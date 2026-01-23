#!/usr/bin/env python3

from icalendar import Calendar, Event
from pytz import timezone
from datetime import datetime
from pathlib import Path

cal = Calendar()
cal.add('prodid', '-//The Arbor Calender Generator//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Arbor Weekly Q&A')
event.add('dtstart', datetime(2023, 5, 10, 13, 0, 0, tzinfo=timezone('Europe/Amsterdam')))
event.add('dtend', datetime(2023, 5, 10, 14, 0, 0, tzinfo=timezone('Europe/Amsterdam')))
event.add('location', 'https://matrix.to/#/#arbor-sim_community:gitter.im')
event.add('LOLWUT',"") #can't add RRULE directly, and args are escaped producing invalid ical...
        
cal.add_component(event)

with open(Path(__file__).parent / 'weekly-meet.ics', 'wb') as f:
    f.write(cal.to_ical().decode("UTF-8").replace("LOLWUT:","RRULE:FREQ=WEEKLY;BYDAY=WE").encode("UTF-8"))
    f.close()
