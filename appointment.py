
class Appointment:
    """
    Uses the information about appointments from the variables to 
    determine if two appointment times overlap. 
    """
    def __init__(self, name, start, end):
        """
        Initializes class variables.
        """
        self.name = name
        self.start = start
        self.end = end

    def overlaps(self, other):
        """
        Returns true or false based on if two appointments overlap.
        """
        return (self.start <= other.start < self.end) or (self.start < other.end <= self.end)


#use_appointment

from appointment import Appointment


def main():
    """ 
    using Appointment class. 
    """
    a1 = Appointment("Math meeting", (9, 30), (10, 45))
    a2 = Appointment("Lunch", (10, 30), (11, 00))
    a3 = Appointment("English Class", (13, 00), (14, 00))
    if a1.overlaps(a2):
        print(f"{a1.name} overlaps with {a2.name}")
    else:
        print(f"{a1.name} does not overlap with {a2.name}")
    if a1.overlaps(a3):
        print(f"{a1.name} overlaps with {a3.name}")
    else:
        print(f"{a1.name} does not overlap with {a3.name}")
    assert a1.overlaps(a2)
    assert a2.overlaps(a1)
    assert not a1.overlaps(a3)
    assert not a3.overlaps(a1)
    assert not a2.overlaps(a3)
    assert not a3.overlaps(a2)


if __name__ == "__main__":
    main()
