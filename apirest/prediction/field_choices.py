MONTH_CHOICES = (
    ("Feb", "February"),
    ("Mar", "March"),
    ("May", "May"),
    ("June", "June"),
    ("Jul", "July"),
    ("Aug", "August"),
    ("Sep", "September"),
    ("Oct", "October"),
    ("Nov", "November"),
    ("Dec", "December")
)

VISITOR_TYPE_CHOICES = (
    ("Returning_Visitor", "Returning visitor"),
    ("New_Visitor", "New visitor"),
    ("Other", "Other")
)

OS_CHOICES = (
    (1, "Windows"),
    (2, "Ubuntu"),
    (3, "Mac OS"),
    (4, "Fedora"),
    (5, "Solaris"),
    (6, "Free BSD"),
    (7, "Chrome OS"),
    (8, "CentOS")
)

BROWSER_CHOICES = (
    (1, "Google Chrome"),
    (2, "Mozilla Firefox"),
    (3, "Safari"),
    (4, "Internet Explorer"),
    (5, "Arachne"),
    (6, "AWeb"),
    (7, "Dillo"),
    (8, "Dooble"),
    (9, "HighWire"),
    (10, "IBrowse"),
    (11, "iCab"),
    (12, "Lunascape"),
    (13, "Konqueror")
)

REGION_CHOICES = (
    (1, "Africa"),
    (2, "North America"),
    (3, "South America"),
    (4, "Eastern Europe"),
    (5, "South Asia and Southeast Asia"),
    (6, "Oceania"),
    (7, "Europe"),
    (8, "Central Asia"),
    (9, "Middle East")
)

from enum import Enum


class MonthNumber(Enum):
    Feb = 1
    Mar = 2
    May = 3
    June = 4
    July = 5
    Aug = 6
    Sep = 7
    Oct = 8
    Nov = 9
    Dec = 10


class VisitorTypeNumber(Enum):
    Returning_Visitor = 0
    New_Visitor = 1
    Other = 2
