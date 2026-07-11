def parse_event(event):
    event = event.strip().upper()
    if not event:
        return None

    if event in ("W", "WK", "OUT"):
        return "wicket", 0, True
    if event in ("NB", "WNB"):
        return "noball", 1, False
    if event in ("WD", "WIDE"):
        return "wide", 1, False
    if event.isdigit():
        runs = int(event)
        if 0 <= runs <= 6:
            return "run", runs, True
    if event.startswith("NB"):
        extra = event[2:]
        if extra.isdigit():
            return "noball", 1 + int(extra), False
        return "noball", 1, False
    if event.startswith("WD"):
        extra = event[2:]
        if extra.isdigit():
            return "wide", 1 + int(extra), False
        return "wide", 1, False
    return None


def format_overs(legal_balls):
    overs = legal_balls // 6
    balls = legal_balls % 6
    return f"{overs}.{balls}"


def main():
    line = input("Enter ball events separated by spaces (e.g. 1 2 4 W NB WD 6): ").strip()
    events = [e for e in line.replace(",", " ").split() if e]
    if not events:
        print("No input provided.")
        return

    legal_balls = 0
    total_runs = 0
    wickets = 0
    extras = 0

    for event in events:
        parsed = parse_event(event)
        if parsed is None:
            print(f"Ignored invalid event: {event}")
            continue

        event_type, value, legal = parsed
        if event_type == "wicket":
            wickets += 1
        elif event_type in ("noball", "wide"):
            extras += value
            total_runs += value
        else:
            total_runs += value

        if legal:
            legal_balls += 1

    print("Scoreboard")
    print("---------")
    print(f"Total runs: {total_runs}")
    print(f"Wickets: {wickets}")
    print(f"Overs: {format_overs(legal_balls)}")
    print(f"Extras: {extras}")


if __name__ == "__main__":
    main()
