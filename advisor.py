import random
class Advisor:
    def __init__(self, name='Freya'):
        self.name = name
        self.last_task_success = None  

    def advise_on_build(self, base):
        direction_map = {'N': 'north', 'S': 'south', 'E': 'east', 'W': 'west', 'Mid': 'mid'}
        all_directions = list(direction_map.keys())

        empty_slots = [d for d in all_directions if d not in base.platforms]

        if empty_slots:
            readable_empty = [direction_map[d] for d in empty_slots]
            return f"{self.name}: Boss, we still have empty slots: {', '.join(readable_empty)}. Let's expand!"
        else:
            return f"{self.name}: Boss, all platforms are occupied! Mother base are strong now!"
    
    def advise_on_money(self, base):
        if base.gold < 2000:
            return f"{self.name}: Boss, our funds are critically low... we should secure more resources!"
        elif base.gold > 3000:
            return f"{self.name}: Boss, we've got a good reserve. Maybe it's time to upgrade platforms?"
        else:
            return f"{self.name}: Boss, we're holding steady. Just say the word!"
        

    def advise_on_task(self, task):
        if task.tier == 'hard':
            choices = [
                f"{self.name}: Boss, this mission is dangerous... please be careful!",
                f"{self.name}: Boss, are you sure about this? It’s really risky!",
                f"{self.name}: I trust you, Boss... but I'm worried.",
            ]
            return random.choice(choices)

        elif task.tier == 'easy':
            choices = [
                f"{self.name}: This one should be manageable. Let’s stay sharp!",
                f"{self.name}: Should be a walk in the park, Boss. But don’t get careless!",
                f"{self.name}: Hehe, this mission looks fun! I’ll cheer you on, Boss!",
            ]
            return random.choice(choices)

        else:  # mid-level
            choices = [
                f"{self.name}: Mid-level mission, Boss. I trust your judgment.",
                f"{self.name}: Not too easy, not too hard — perfect for sharpening our skills!",
                f"{self.name}: Boss, this could go either way. Let’s stay focused!",
            ]
            return random.choice(choices)

    def after_task(self, success):
    
        if success:
            self.last_task_success = True
            choices = [
                f"{self.name}: Great job, Boss! We're one step closer!",
                f"{self.name}: Well done! The team’s morale is sky-high!",
                f"{self.name}: You never fail to impress, Boss!",
                f"{self.name}: Boss, you’re amazing! I’m proud to be your support!",
            ]
            return random.choice(choices)
        else:
            self.last_task_success = False
            choices = [
                f"{self.name}: Don't worry, Boss... we'll learn from this and come back stronger!",
                f"{self.name}: We’ll recover, Boss. I believe in you!",
                f"{self.name}: It’s okay, Boss... setbacks happen. Let’s push on!",
                f"{self.name}: Boss... I’m always here for you, no matter what.",
            ]
            return random.choice(choices)
        
    def advise_on_success_rate(self, task):
        if task.success_rate < 0.5:
            return (f"{self.name}: Boss, this mission has a low success rate "
                    f"({task.success_rate * 100:.1f}%). I recommend improving our base first, "
                    "perhaps by constructing additional platforms.")
        else:
            return (f"{self.name}: Success rate looks reasonable "
                    f"({task.success_rate * 100:.1f}%). Ready when you are, Boss!")