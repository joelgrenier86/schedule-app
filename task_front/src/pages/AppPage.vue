

<template>
  <div class="subcontent">


      <div class="column" v-if="currentPage=='login'">
        <div class="row justify-center">
          <h5 class="text-h5 text-center q-my-md ">Schedule App</h5>
        </div>
        <div class="row justify-center">
          <q-card square bordered class="q-pa-lg bg-primary shadow-1">
        
              <q-form class="q-gutter-md" @submit="onLogin">
                <q-input square filled clearable v-model="email" type="email" label="email" class = "bg-white"/>
             
            
          
              <q-btn elevated color="light-blue-6" size="lg" class="full-width" type="submit" label="Login" />
            </q-form>
          
            <q-card-section class="text-center q-pa-none">
              <p class="text-grey-6">Enter your email to book a meeting</p>
            </q-card-section>
          </q-card>
        </div>
      </div>

    <div class="row justify-center" v-if="currentPage=='month'">
      <div style="display: flex; max-width: 800px; width: 100%;">
        <q-calendar-month
          ref="calendar"
          v-model="selectedDate"
          :day-min-height="40"
          animated
          bordered
          @change="onChange"
          @moved="onMoved"
          @click-date="onClickDate"
          @click-day="onClickDay"
          @click-workweek="onClickWorkweek"
          @click-head-workweek="onClickHeadWorkweek"
          @click-head-day="onClickHeadDay"
        />
        
      </div>
    </div>
    <div class="row justify-center" v-if="currentPage=='day'">
      <div style="display: flex; max-width: 800px; width: 100%; height: 400px;">
        <q-calendar-day
          ref="calendar"
          v-model="selectedDate"
          view="day"
          :interval-minutes="30"
          :interval-count="48"
        
          bordered
          animated
          time-clicks-clamped
          @change="onChange"
          @moved="onMoved"
          @click-date="onClickDate"
          @click-time="onClickTime"
          @click-interval="onClickInterval"
          @click-head-intervals="onClickHeadIntervals"
          @click-head-day="onClickHeadDay"
        >
        <template #day-body="{ scope: { timestamp, timeStartPos, timeDurationHeight } }"> 
        
            <template
              v-for="event in getEvents(timestamp.date)"
              
            >
            
            <div
                :key="event.id"
                v-if="event.time !== undefined"
                  :class="badgeClasses(event)"
                  :style="badgeStyles(event, timeStartPos, timeDurationHeight)"
                  class="my-event row"
                >
                <q-btn v-if="event.client_id == this.user.id || this.user.admin" @click="onChangeMeeting(event)" label="Change" type="submit" color="primary" />
                
                
                
                <div class="title q-calendar__ellipsis">
                
                  <q-tooltip>{{ event.time + ' - ' + event.note }}</q-tooltip>
                </div>
                
              
            
              </div>
          </template>
          </template>
        </q-calendar-day>
      </div>
    </div>
    <div>
      
    </div>
    <div class="row justify-center" v-if="currentPage=='bookMeeting'">
      <q-form
      @submit="onSubmitMeeting"
      @reset="onBack"
      class="q-gutter-md"
    >
      <q-input
        filled
        v-model="note"
        label="Note *"
        hint="Add a note"
        lazy-rules
        :rules="[ val => val && val.length > 0 || 'Please enter a note']"
      />



   
        {{details}}
      <div>
        <q-btn v-if="details='create'" label="Submit" type="submit" color="primary"/>
        <q-btn v-if="details='edit'" label="Edit" action="editMeeting" color="primary"/>
        <q-btn v-if="details='edit'" label="Delete" action="deleteMeeting" color="primary"/>
        <q-btn label="Back" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>

    </div>
  </div>
</template>

<script>
import { QCalendarMonth, QCalendarDay, getDayTimeIdentifier,getDateTime, today, getDate, parseDate, parseTime } from '@quasar/quasar-ui-qcalendar/src/index.js'
import '@quasar/quasar-ui-qcalendar/src/QCalendarVariables.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarTransitions.sass'
import '@quasar/quasar-ui-qcalendar/src/QCalendarMonth.sass'
import { defineComponent } from 'vue'
import { api } from 'boot/axios'


export default {
  name: 'AppPage',
  components: {
    QCalendarMonth,
    QCalendarDay
  },
  
  
  data () {
    return {
      selectedDate: today(),
      currentPage: String,
      selected: [],
      note:String,
      email:String,
      dates:[],
      meetings:[],
      users:[],
      user:{},
      details:String
      

   
    }
  },
  methods: {
    onToday () {
      this.$refs.calendar.moveToToday()
    },
    onPrev () {
      this.$refs.calendar.prev()
    },
    onNext () {
      this.$refs.calendar.next()
    },
    onMoved (data) {
      console.log('onMoved', data)
    },
    onChange (data) {
      console.log('onChange', data)
    },
    onClickDate (data) {
      console.log('onClickDate', data)
      this.currentPage = "day"
    },
    onClickDay (data) {
      console.log('onClickDay', data)
    },
    onClickWorkweek (data) {
      console.log('onClickWorkweek', data)
    },
    onClickHeadDay (data) {
      console.log('onClickHeadDay', data)
    },
    onClickHeadWorkweek (data) {
      console.log('onClickHeadWorkweek', data)
    },
    onChangeMeeting(event){
      this.meeting = event
      this.currentPage = "bookMeeting"
      this.details = "edit"
    },
    onClickTime (data) {
      console.log('onClickTime', data.scope.timestamp)
      this.selected = data.scope.timestamp
      this.currentPage = "bookMeeting"        
      },
    
    
    
    onClickInterval (data) {
      console.log('onClickInterval', data)
    },
    onSubmitMeeting(){
      console.log(this.note)
      const url = 'users/' + this.user.id +'/meetings/'
      const meeting = { note: this.note, time: getDateTime(this.selected) };
      api.post(url, meeting)
        .then(response => this.meetingId = response.data.id);
    },
    onLogin(){
  
      this.users.forEach((user)=>{
        if (this.email == user.email){
          this.user = user
          this.currentPage = 'month'
          return console.log(this.user)
        }
      }
      )
  
      
    },
    badgeClasses (event) {
  
      
      if (event.client_id == this.user.id || this.user.admin){
      return {
        [ `text-white bg-primary` ]: true,

        'rounded-border': true
      }
      }
      else{
        return {
        [ `my-event text-white bg-grey` ]: true,
        'rounded-border': true
      }
      }
    },
    badgeStyles (event,  timeStartPos = undefined, timeDurationHeight = undefined) {
      const s = {}
      let t = new Date(event.time)
       //somewhere along teh way i have a timezone thats placing the meetings 5 hours later than they should be, hack fix below
       //bug still exists but has changed (:
        t.setHours(t.getHours() - 5)
        let splitDate =  t.toISOString().split( "T" )
        let formTime = splitDate[1].split(":")
   
      
       
        formTime[0] = formTime + 5
        
        formTime = formTime[0] +':' + formTime[1]
      let time = event.time
      if (timeStartPos && timeDurationHeight) {
        //if you dont set position to absolute, as I eventually did in a seperate css class, the meeting boxes will be underneath the last time segment
        //dont make that mistake!

        s.top = timeStartPos(formTime) + 'px'
        s.height = timeDurationHeight(30) + 'px'
        s.left = "0"
        s.width = "99%"
      }
      s[ 'align-items' ] = 'flex-start'
      
      return s
    },
    getEvents (day) {
      let ret    = []
     console.log(this.user.id)
      // get all events for the specified date
      this.meetings.forEach((meeting)=>{
        
        let t = new Date(meeting.time)
        
        let splitDate =  t.toISOString().split( "T" )
       
        if (splitDate[0] == day){
   
          ret.push(meeting)
         
        }
      })
     
      
     
      return ret
    },
    onBack(data){
      this.currentPage = "month"
    },
    onClickHeadIntervals (data) {
      console.log('onClickHeadIntervals', data)
      this.currentPage = "month"
    },

  },
  created() {
    this.currentPage = "day"
    this.details = "create"
    this.note = ""
    this.dates = []
    this.email = ""
  
    api.get('meetings/')
                .then(response =>{
                  this.meetings = response.data
                  
                })
                .catch(e => {
                  console.log(e)
                })
    api.get('users/')
    .then(response =>{
                  this.users = response.data
                  this.user = this.users[1]
                })
                .catch(e => {
                  console.log(e)
                })
          
              
           
  },

  computed: {
    selectedDates(){
      const dateList = []
     
      this.meetings.forEach((meeting)=>{
        let time = meeting.time
        if(meeting.clientid == this.user.id || this.user.admin ){
         
          dateList.push(time)
          
        }
      })
      
      return dateList
    },
    blockedDates(){
      const bad = []
      this.meetings.forEach((meeting)=>{
        let time = meeting.time
        if(meeting.clientid != this.email && !this.user.admin){
          bad.push(time)
        }
      })
     
    return bad

    }
  }
}
</script>

