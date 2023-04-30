#include "countingdays.h"

int p = 0, days = 1;

void lookAtClock(int hours, int minutes) {
    int t = hours * 60 + minutes;
    if (t < p) days += 1;
    p = t;
}

int getDay() {
    return days;
}
