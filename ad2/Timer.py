#!/usr/bin/env python
# coding: UTF-8
#
# @package Timer
# @author Ariadne Pinheiro
# @date 08/10/2020
#
# Keep packing (drawing) circles, after a certain time interval.
#
##

class Timer:
    # Keep packing (drawing) circles, after a certain time interval.
    def __init__(self, root, callback, delay):
        self.root = root
        self.callback = callback
        self.delay = delay
        self.task = None

    def run(self):
        # Run the callback function every delay ms.
        self.callback()
        self.task = self.root.after(self.delay, self.run)

    def stop(self):
        # Stop the drawing process.
        if self.task is not None:
            self.root.after_cancel(self.task)
            self.task = None

    def restart(self):
        # Restart the drawing process.
        self.stop()
        self.run()
