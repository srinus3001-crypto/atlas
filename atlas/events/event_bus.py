"""
Atlas Event Bus

Simple in-memory enterprise event bus.
"""

from collections import defaultdict

from atlas.core.logger import Logger


class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, handler):
        self.listeners[event_type].append(handler)

    def publish(self, event):
        Logger.info(f"EVENT -> {event.event_type}")

        handlers = self.listeners.get(event.event_type, [])

        for handler in handlers:
            handler(event)


event_bus = EventBus()
