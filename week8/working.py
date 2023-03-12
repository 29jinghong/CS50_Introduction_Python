import re


def main():
    print(find(input("Hours: ")))


def find(time):
    matches = re.search(
        r"^"
        r"("
        r"(?:\d|1[0-2])"  
        r"(?::[0-5]\d)?" 
        r" ([AP]M)"
        r" to "
        r"((?:\d|1[0-2]|\d|1[0-2])(?::[0-5]\d)?) ([AP]M)$",
        time
    )

    start = {"hr": matches.group(1), "AMPM": matches.group(2)}
    end = {"hr": matches.group(3), "AMPM": matches.group(4)}
    return(convert(start),convert(end))

def convert(time):
    if ":" in time["hr"]:
        hr, min = map(int, time["hr"].split(":"))
        if time["AMPM"] == "AM":
            time_24 = (
                f"{(hr - 12):02}:{hr:02}"
                if hr == 12
                else f"{hr:02}:{min:02}"
            )
        else:
            time_24 = (
                f"{hr:02}:{min:02}"
                if hr == 12
                else f"{(hr + 12):02}:{min:02}"
            )
    else:
        hr = int(time["time"])
        min = 0
        if time["meridiem"] == "AM":
            if hr == 12:
                time_24 = f"{(hr - 12):02}:{min:02}"
            else:
                time_24 = f"{hr:02}:{min:02}"
        else:
            if hr == 12:
                time_24 = f"{hr:02}:{min:02}"
            else:
                time_24 = f"{(hr + 12):02}:{min:02}"

    return time_24

if __name__ == "__main__":
    raise SystemExit(main())
