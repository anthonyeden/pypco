"""PCO CheckIns endpoints.

Generated by pypco_generator tool. Manual changes not recommended.
"""

#pylint: disable=C0304,R0903,C0111,C0321

from .base_endpoint import BaseEndpoint

# The base CheckIns endpoint
class CheckInsEndpoint(BaseEndpoint): pass

# All CheckIns endpoints
class CheckIns(CheckInsEndpoint):
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
    pass

class EventTimes(CheckInsEndpoint):
    """A time that someone may check in. Times are copied from session to session.
"""
    pass

class Events(CheckInsEndpoint):
    """A recurring event which people may attend.

Each recurrence is an _event period_ (which often corresponds to a week).

Event periods have _event times_ where people may actually check in.
"""
    pass

class Headcounts(CheckInsEndpoint):
    """A tally of attendees for a given event time and attendance type.
If one does not exist, the count may have been zero.
"""
    pass

class Labels(CheckInsEndpoint):
    """Labels can be set to print for events (through `EventLabel`s),
locations (through `LocationLabel`s) or options.
Label type (security label / name label) is expressed with the
`prints_for` attribute. `prints_for="Person"` is a name label,
`prints_for="Group"` is a security label.
"""
    pass

class Passes(CheckInsEndpoint):
    """Enables quick lookup of a person via barcode reader.
"""
    pass

class People(CheckInsEndpoint):
    """An attendee, volunteer or administrator.

_Usually_, a person who checked in will be present as a `Person`. In some cases, they may not be present:
- The person was manually deleted from the admin interface
- The check-in was created as a "One-time guest" (which doesn't create a corresponding person record)

"""
    pass

class Stations(CheckInsEndpoint):
    """A device where people can be checked in.
A device may also be connected to a printer
and print labels for itself or other stations.
"""
    pass

class Themes(CheckInsEndpoint):
    """A custom style which may be applied to stations.
"""
    pass
