from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, to, msg):
        pass

    @property
    def cost_paise(self):
        return 0


class WhatsAppNotifier(Notifier):

    def send(self, to, msg):
        return f"Whatsapp->sending msg: {to}, {msg}"

    @property
    def cost_paise(self):
        return 35

class EmailNotifier(Notifier):

    def send(self, to, msg):
        return f"Email->sending msg: {to}, {msg}"

    @property
    def cost_paise(self):
        return 1


class SmsNotifier(Notifier):
    MAX = 160

    def send(self, to, msg):
        if len(msg) > self.MAX:
            msg = msg[:self.MAX - 3] + "..."
        return f"[SMS -> {to}] {msg}"

    @property
    def cost_paise(self):
        return 18


def broadcast(notifier, learners, msg):
    total_cost = 0

    for learner in learners:
        notifier.send(learner, msg)
        total_cost += notifier.cost_paise

    return total_cost


learners = [
    f"+9198765432{i:02d}"
    for i in range(18)
]

reminder = (
    "Reminder: your upcoming session starts tomorrow at 10:00 AM IST sharp. "
    "Please bring your assignment-03 repository link and make sure your code "
    "is pushed and ready for review. Do not miss the session!"
)

print("Message length:", len(reminder))

for notifier in [ WhatsAppNotifier(), EmailNotifier(), SmsNotifier() ]:
    cost  = broadcast(notifier, learners, reminder)
    print(f"{notifier.__class__.__name__}: {cost} paise")