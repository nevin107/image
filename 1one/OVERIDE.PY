class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate

    def compute_pay(self, hours):
        pass


class DailyWorker(Worker):
    def compute_pay(self, days):
        return self.salary_rate * days


class SalariedWorker(Worker):
    def compute_pay(self, hours):
        weekly_hours = 40
        if hours <= weekly_hours:
            return self.salary_rate * hours
        else:
            return self.salary_rate * weekly_hours


# Example usage:
daily_worker = DailyWorker("John", 50)
daily_pay = daily_worker.compute_pay(5)  # Assuming John worked for 5 days
print("Daily Worker Pay:", daily_pay)

salaried_worker = SalariedWorker("Alice", 1000)
salaried_pay = salaried_worker.compute_pay(45)  # Assuming Alice worked for 45 hours
print("Salaried Worker Pay:", salaried_pay)
