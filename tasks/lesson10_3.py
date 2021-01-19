"""
Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel 
    numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last 
    one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the 
    first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and 
    returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

The default channel turned on before all commands is #1.
"""


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.active_channel = 0

    def first_channel(self):
        self.active_channel = 0
        return self.channels[self.active_channel]

    def last_channel(self):
        # self.active_channel = len(self.channels)-1
        self.active_channel = -1
        return self.channels[self.active_channel]

    def turn_channel(self, N):
        if N is None or N >= len(self.channels):
            raise ValueError("Unknown channel")

        self.active_channel = N-1
        return self.channels[self.active_channel]

    def next_channel(self):
        if self.active_channel == len(self.channels)-1:
            self.active_channel = 0
        else:
            self.active_channel += 1

        return self.channels[self.active_channel]

    def previous_channel(self):
        if self.active_channel == 0:
            self.active_channel = len(self.channels)-1
        else:
            self.active_channel -= 1

        return self.channels[self.active_channel]

    def current_channel(self):
        return self.channels[self.active_channel]

    def is_exist(self, channel):
        if (isinstance(channel, int) and 1 < channel < len(self.channels)+1) \
                or channel in self.channels:
            return "YES"
        else:
            return "NO"


channels = ["BBC", "Discovery", "TV1000"]

controller = TVController(channels)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
