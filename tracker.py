
import data


def add_session():
    """Collect information and save a study session."""
    subject = input("Enter subject/course: ").strip()

    if not subject:
        print("Subject cannot be empty.")
        return

    try:
        minutes = int(input("Enter minutes studied: "))
        if minutes <= 0:
            print("Minutes must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid whole number of minutes.")
        return

    location = input("Enter location (Home/Library/Lab/Other): ").strip()
    if not location:
        print("Location cannot be empty.")
        return

    session_notes = input("Enter notes (optional): ").strip()

    # Add each value at the same index in its parallel list.
    data.subjects.append(subject)
    data.minutes_studied.append(minutes)
    data.locations.append(location)
    data.notes.append(session_notes)

    print("Session added.")


def view_all():
    """Display every saved study session."""
    if not data.subjects:
        print("No study sessions recorded yet.")
        return

    print("\n--- All Study Sessions ---")

    for i in range(len(data.subjects)):
        print(f"\nSession {i + 1}")
        print(f"Subject: {data.subjects[i]}")
        print(f"Minutes: {data.minutes_studied[i]}")
        print(f"Location: {data.locations[i]}")
        print(f"Notes: {data.notes[i] or 'None'}")


def view_summary():
    """Display statistics about recorded study sessions."""
    total_sessions = len(data.subjects)

    if total_sessions == 0:
        print("No study sessions available for a summary.")
        return

    total_minutes = sum(data.minutes_studied)
    average_minutes = total_minutes / total_sessions
    longest = max(data.minutes_studied)
    shortest = min(data.minutes_studied)

    print("\n--- Study Session Summary ---")
    print(f"Total sessions: {total_sessions}")
    print(f"Total minutes studied: {total_minutes}")
    print(f"Average minutes per session: {average_minutes:.1f}")
    print(f"Longest session: {longest} minutes")
    print(f"Shortest session: {shortest} minutes")
