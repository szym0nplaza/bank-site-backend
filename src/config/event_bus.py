import asyncio, json, uuid, time
from config.settings import RabbitMQClient


class EventBus:
    """Event Bus is base class for processing events through app modules"""

    def __init__(self, rabbitmq_client=RabbitMQClient("bank-app")):
        self.rabbitmq_client = rabbitmq_client
        self.listeners = {}  # {event_name: handler(function)}
        self._responses = {}

    def add_listener(self, event_name: str, listener) -> None:
        if not self.listeners.get(event_name, None):
            self.listeners[event_name] = {listener}
        else:
            self.listeners[event_name].add(listener)

    def remove_listener(self, event_name: str) -> None:
        del self.listeners[event_name]

    def get_response_value(self, event_name: str):
        while True:
            time.sleep(0.05)
            if event_name in self._responses.keys():
                return self._responses.get(event_name)

    async def process_incoming_event(self, message):
        await message.ack()
        body = message.body
        body = json.loads(body)
        response = self.listeners[body.get("event_name")](body.get("params"))
        if response:
            self._responses[body.get("event_name")] = response

    async def consume(self, loop):
        await self.rabbitmq_client.consume(loop, self.process_incoming_event)

    def run_event(self, message: dict):
        self.corr_id = uuid.uuid4()
        self.rabbitmq_client.channel.basic_publish(
            exchange="",
            routing_key=self.rabbitmq_client.queue_name,
            body=json.dumps(message),
        )


event_bus = EventBus()
loop = asyncio.get_running_loop()
loop.create_task(event_bus.consume(loop))
