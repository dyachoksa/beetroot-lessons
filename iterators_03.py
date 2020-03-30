
class Boss:
    def __init__(self, name, workers = []):
        self.name = name
        self.workers: list = workers
        self.worker_it = None

    def __iter__(self):
        self.worker_it = iter(self.workers)
        return self

    def __next__(self):
        return next(self.worker_it)

    def add_worker(self, name):
        self.workers.append(name)


boss = Boss("Me")

boss.add_worker("Worker 1")
boss.add_worker("Worker 2")
boss.add_worker("Worker 3")

for worker in boss:
    print(worker)

boss.add_worker("Secretary 1")
print(list(boss))
