"""PCO CheckIns models.

Generated by pypco_generator tool. Manual changes not recommended.
"""

#pylint: disable=C0321,R0903,C0111

from .base_model import BaseModel

# The base CheckIns model
class CheckInsModel(BaseModel): pass

# CheckIns Models
class AttendanceType(CheckInsModel): 
    """A kind of attendee which is tracked by _headcount_, not by check-in.
"""
    ENDPOINT_NAME='events'

class CheckIn(CheckInsModel): 
    """An attendance record for an event.

If someone was checked out, `checked_out_at` will be present.

You can scope check-ins in a few ways:

- `regular`s, `guest`s, and `volunteer`s correspond to the option selected when checking in.
- `attendee`s are `regular`s and `guest`s together.
- `one_time_guest`s are check-ins which were created without a corresponding person record.
- `not_one_time_guest`s are check-ins which had a corresponding person record when they were created.
- `checked_out` are check-ins where `checked_out_at` is present (meaning they were checked out from a station).
- `first_time`s are check-ins which are the person's first for a given event. (One-time guests are not included here.)
"""
    ENDPOINT_NAME='check_ins'

class CheckInGroup(CheckInsModel): 
    """When one or more people check in, they're grouped in a `CheckInGroup`.
These check-ins all have the same "checked-in by" person. `CheckInGroup` is also
the basis for label printing.

`print_status` may be:

- `ready`: This group isn't printed or canceled yet
- `printed`: This group was successfully printed at a station
- `canceled`: This group was canceled at a station
- `skipped`: This group had no labels to print, so it was never printed.
"""
    ENDPOINT_NAME='check_ins'

class Event(CheckInsModel): 
    """A recurring event which people may attend.

Each recurrence is an _event period_ (which often corresponds to a week).

Event periods have _event times_ where people may actually check in.
"""
    ENDPOINT_NAME='events'

class EventLabel(CheckInsModel): 
    """Says how many of a given label to print for this event and
whether to print it for regulars, guests, and/or volunteers.
"""
    ENDPOINT_NAME='events'

class EventPeriod(CheckInsModel): 
    """A recurrence of an event, sometimes called a "session".
For weekly events, an event period is a week. For daily events, an event period is a day.
An event period has event times, which is what people select
when they actually check in. When new sessions are created, times
are copied from one session to the next.
"""
    ENDPOINT_NAME='check_ins'

class EventTime(CheckInsModel): 
    """A time that someone may check in. Times are copied from session to session.
"""
    ENDPOINT_NAME='event_times'

class Headcount(CheckInsModel): 
    """A tally of attendees for a given event time and attendance type.
If one does not exist, the count may have been zero.
"""
    ENDPOINT_NAME='headcounts'

class Label(CheckInsModel): 
    """Labels can be set to print for events (through `EventLabel`s),
locations (through `LocationLabel`s) or options.
Label type (security label / name label) is expressed with the
`prints_for` attribute. `prints_for="Person"` is a name label,
`prints_for="Group"` is a security label.
"""
    ENDPOINT_NAME='labels'

class Location(CheckInsModel): 
    """A place where people may check in to for a given event.
Some locations have `kind="Folder"`, which means that people
can't check-in here, but this location contains other locations.
You can get its contents from the `locations` attribute.
You can get a location's parent folder from the `parent` attribute.
(If it's not in a folder, `parent` will be empty.)
"""
    ENDPOINT_NAME='check_ins'

class LocationEventPeriod(CheckInsModel): 
    """Counts check-ins for a location during a certain event period.
"""
    ENDPOINT_NAME='check_ins'

class LocationEventTime(CheckInsModel): 
    """Counts check-ins for a location for a given event time.
This is useful for checking occupancy.
"""
    ENDPOINT_NAME='event_times'

class LocationLabel(CheckInsModel): 
    """Says how many of a given label to print for this location and
whether to print it for regulars, guests, and/or volunteers.
"""
    ENDPOINT_NAME='labels'

class Option(CheckInsModel): 
    """An option which an attendee may select when checking in.

Options may have extra labels associated with them, denoted by `label` and `quantity`.
"""
    ENDPOINT_NAME='check_ins'

class Pass(CheckInsModel): 
    """Enables quick lookup of a person via barcode reader.
"""
    ENDPOINT_NAME='passes'

class Person(CheckInsModel): 
    """An attendee, volunteer or administrator.

_Usually_, a person who checked in will be present as a `Person`. In some cases, they may not be present:
- The person was manually deleted from the admin interface
- The check-in was created as a "One-time guest" (which doesn't create a corresponding person record)

"""
    ENDPOINT_NAME='people'

class PersonEvent(CheckInsModel): 
    """Counts a person's attendence for a given event.
"""
    ENDPOINT_NAME='events'

class Station(CheckInsModel): 
    """A device where people can be checked in.
A device may also be connected to a printer
and print labels for itself or other stations.
"""
    ENDPOINT_NAME='stations'

class Theme(CheckInsModel): 
    """A custom style which may be applied to stations.
"""
    ENDPOINT_NAME='themes'
