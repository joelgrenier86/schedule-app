

<template>
  <div class="subcontent">

    
    <div class="column">
      <div class="row">
        <h5 class="text-h5 text-white q-my-md">Company & Co</h5>
      </div>
      <div class="row">
        <q-card square bordered class="q-pa-lg shadow-1">
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input square filled clearable v-model="email" type="email" label="email" />
              <q-input square filled clearable v-model="password" type="password" label="password" />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn unelevated color="light-green-7" size="lg" class="full-width" label="Login" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">Not reigistered? Created an Account</p>
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
          :interval-minutes="30"
          :interval-count="48"
          :selected-dates="selectedDates"
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
        />
      </div>
    </div>
    <div>
      
    </div>
    <div class="row justify-center" v-if="currentPage=='bookMeeting'">
      <q-form
      @submit="onSubmit"
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



   

      <div>
        <q-btn label="Submit" type="submit" color="primary"/>
        <q-btn label="Back" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>

    </div>
  </div>
</template>

<script>
import { QCalendarMonth, QCalendarDay, getDayTimeIdentifier,getDateTime, today } from '@quasar/quasar-ui-qcalendar/src/index.js'
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
      meetings:[]

   
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
    onClickTime (data) {
      console.log('onClickTime', data.scope.timestamp)
      this.selected = data.scope.timestamp
      this.currentPage = "bookMeeting"        
      },
    
    
    
    onClickInterval (data) {
      console.log('onClickInterval', data)
    },
    onSubmit(data){
      console.log(this.note)
      const url = 'users/1/meetings/'
      const meeting = { note: this.note, time: getDateTime(this.selected) };
      api.post('users/1/meetings/', meeting)
        .then(response => this.meetingId = response.data.id);
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
    this.currentPage = "login"
    this.note = ""
    this.dates = []
    api.get('meetings/')
                .then(response =>{
                  this.meetings = response.data
              
                })
                .catch(e => {
                  console.log(e)
                })
               
              
           
  },
  computed: {
    selectedDates(){
      const dateList = []
     dateList.push(getDateTime(this.selected))
      return dateList
    }
  }
}
</script>

