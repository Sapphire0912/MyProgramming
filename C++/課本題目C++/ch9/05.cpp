#include<iostream>
using namespace std;

class Time {
	public:                 
  		Time(int h=12,int m=0,int s=0){hour = h; min = m; sec = s;}
  		void set(int h,int m,int s){hour = h; min = m; sec = s;}
  		void show();
	private:
  		int hour, min, sec;   
};

class Clock {
	public:
  		Clock(int h,int m,int s=0){clock_time.set(h,m,s);}
  		void show();
  		void setAlarm(int h,int m,int s=0){alarm_time.set(h,m,s);}
	private:
  		Time clock_time;     
  		Time alarm_time;     
};

void Time::show(){
	cout << hour << ":" << min << ":" << sec << '\n';
}

void Clock::show(){
	cout << "Now Time: ";
	clock_time.show();
	cout << "Alarm set time: ";
	alarm_time.show();
}

int main(){
  Clock old_clock(12,34,56);
  old_clock.setAlarm(8,30);
  old_clock.show();
}
