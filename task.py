




import random
import time

class Task:
    
    def __init__(self, name ,description, base_success, reward, bonus, cost, tier='unknown'):

        self.name = name
        self.description= description
        self.success_rate = min(1.0, base_success + bonus)
        self.reward = reward
        self.cost = cost
        self.tier = tier



    def mission_start(self,base):

        if base.gold < self.cost:

            print(f'[WARNING] FUNDING SHORTAGE: Required — {self.cost} credits. Available — {base.gold} credits.')
            print("[INFO] Tactical deployment halted. Awaiting commander override.")
            return 0
        
        base.gold -= self.cost

        #######   mission start text
        #######

        print(f"[EXECUTED] Deployment cost: {self.cost} credits.")
        print(f"[STATUS] Remaining balance: {base.gold} credits.")
        print('')
        time.sleep(2)

        print(f'[INFO] Deploying......')
        time.sleep(2)
        print('')
        print("[SOUND] Rotor blades spinning... *WHIRRRR*")
        time.sleep(0.5)
        print("[SOUND] Engine humming... *BZZZZZZ*")
        time.sleep(0.5)
        print("[SOUND] Landing gear engaged... *CLUNK*")
        time.sleep(0.5)
        print("[SOUND] Preparing for liftoff... *VMMM*")
        time.sleep(0.5)
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║                     -----------!-----------               ║")
        print("║              -----------!-----------  /=====\\             ║")
        print("║                       |===\\_________/_  o  |              ║")
        print("║                       /_]    o o  o o____   /             ║")
        print("║                      <_]___[]_______<____>/               ║")
        print("║                          o              o                 ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print('')
        time.sleep(2)
        print("Pilot: Be careful down there, Boss!")
        print('')
        time.sleep(2)

        print(f'Mission start : {self.name}')
        print('')
        time.sleep(3)

        print(f"Mission information : {self.description}")
        print('')
        time.sleep(3)

        print("[ACTION] Initiating stealth approach...")
        time.sleep(0.5)
        print('....')
        time.sleep(2)
        
        print("[ACTION] Sabotaging local power generator...")
        time.sleep(0.5)
        print('....')
        time.sleep(2)

        print("[ACTION] Neutralizing enemy sentry with tranquilizer...")
        time.sleep(0.5)
        print('....')
        time.sleep(2)

        print("[ACTION] Commencing enemy personnel extraction...")
        time.sleep(0.5)
        print('....')
        time.sleep(2)
        print("[ACTION] Recovering enemy resources...")
        time.sleep(0.5)
        print('....')
        time.sleep(0.5)
        print('')
        print('')
        print('')
        time.sleep(3)

        ######
        ######  text end 

        success = random.random() < self.success_rate

        if success:
            print(f"[INFO] Mission accomplished. Objective achieved. Returning to Mother Base.  Reward is {self.reward} ")

            return self.reward
        
        else:
            #fail

            print("╔══════════╗")
            print("║    ┏┓    ║")
            print("║    ┃┃    ║")
            print("║    ┃┃    ║")
            print("║    ┗┛    ║")
            print("║    ┏┓    ║")
            print("║    ┗┛    ║")
            print("╚══════════╝")
            print('')
            print('')
            print('')
            time.sleep(2)


            ####### list of failure dialogues


            failure_dialogues = [
            # 标准巡逻发现
                [
                    "[RADIO] Patrol: HQ, come in! I've spotted an intruder!",'',
                    "[RADIO] HQ: This is HQ. Confirm the sighting. Are you sure?",'',
                    "[RADIO] Patrol: Affirmative! Unknown unit, moving fast! Requesting backup!",'',
                    "[RADIO] HQ: Roger that. All units, proceed to alert phase. Secure the perimeter!",'',
                ],
                # 交火状况
                [
                    "[RADIO] Patrol: HQ! We're under heavy fire! It's not just one guy!",'',
                    "[RADIO] HQ: This is HQ! Stay calm! Hold your ground!",'',
                    "[RADIO] Patrol: We need reinforcements NOW!",'',
                    "[RADIO] HQ: All units, converge on Patrol's location!",'',
                ],
                # HQ 冷笑话
                [
                    "[RADIO] Patrol: HQ, we’ve got a situation here...",'',
                    "[RADIO] HQ: This is HQ. Wait — don’t tell me, it’s a Cyborg Ninja with a sword, right?",'',
                    "[RADIO] Patrol: Negative! It’s just a regular intruder!",'',
                    "[RADIO] HQ: Phew... For a moment, I thought we were about to be diced into sushi.",'',
                ],
                # 潜行盒子
                [
                    "[RADIO] Patrol: HQ! We just saw... a cardboard box moving?!",'',
                    "[RADIO] HQ: This is HQ. A cardboard box? Are you sure you’re okay?",'',
                    "[RADIO] Patrol: It’s crawling! It’s heading to the supply room!",'',
                    "[RADIO] HQ: ...Deploy the anti-box unit.",'',
                ]
            ]

            selected_dialogue = random.choice(failure_dialogues)
            for line in selected_dialogue:
                print(line)
                time.sleep(1.5)


            
            print(f'[WARNING] Mission failed. Objective incomplete. Proceed to the extraction point.')

            return 0


class TaskManager:

    def __init__(self, base):
        
        self.base = base
    
    def calculate_bonus(self, task_type):

        #calcuate the chance of mission success which add the bone of each platform        
        platform_bonus = {'Intelligence Unit': {'recon': 0.23},
                          'Medic Unit': {'support': 0.25},
                          'Support Unit': {'combat': 0.22},
                          'Development Unit': {'tech': 0.25}}
        
        #####inital bone == 0
        
        total_bonus = 0

        for platform in self.base.platforms.values():

            bonus = platform_bonus.get(platform, {}).get(task_type, 0)
            total_bonus += bonus
        ####out put bonus
        return total_bonus
    
    def task_list(self):

        #return a list which use for class task

        return [
        # easy tier
        Task("Border Recon", "Patrol the perimeter to detect infiltration routes.", 0.60, 150, self.calculate_bonus('recon'), 0, tier='easy'),
        Task("Supply Run", "Deliver essential supplies to the forward operating base.", 0.60, 180, self.calculate_bonus('support'), 60, tier='easy'),
        Task("Radio Intercept", "Tap into enemy communications to gather low-level intel.", 0.60, 200, self.calculate_bonus('tech'), 70, tier='easy'),

        # middle tier
        Task("Frontline Fire Support", "Provide suppressive fire for advancing squads.", 0.40, 400, self.calculate_bonus('combat'), 120, tier='medium'),
        Task("Sabotage Raid", "Infiltrate enemy supply lines and disrupt logistics.", 0.40, 450, self.calculate_bonus('recon'), 130, tier='medium'),
        Task("Combat Extraction", "Rescue a trapped allied unit under heavy enemy fire.", 0.40, 420, self.calculate_bonus('support'), 110, tier='medium'),

        # difficult tier
        Task("Eliminate Elite Unit", "Neutralize a high-value enemy squad and recover critical intel.", 0.28, 700, self.calculate_bonus('combat'), 200, tier='hard'),
        Task("Deep Infiltration", "Penetrate enemy HQ to steal top-secret data undetected.", 0.28, 900, self.calculate_bonus('recon'), 250, tier='hard'),
        Task("Black Site Destruction", "Destroy a clandestine lab to prevent next-gen weapon development.", 0.28, 1000, self.calculate_bonus('tech'), 280, tier='hard')
    ]







        



if __name__ == "__main__":
    '''
    base = Base()
    task_manager = TaskManager(base)
    tasks = task_manager.task_list()

    # 显示任务列表
    print("\nAvailable Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. [{task.tier.upper()}] {task.name} - Cost: {task.cost}, Reward: {task.reward}, Success Rate: {task.success_rate:.2f}")

    # 测试执行第一个任务
    selected_task = tasks[8]
    print("\n--- Executing First Task ---")
    reward = selected_task.mission_start(base)

    if reward:
        base.gold += reward
        print(f"[RESULT] Reward collected. New balance: {base.gold} credits.")
    else:
        print(f"[RESULT] No reward collected. Current balance: {base.gold} credits.")
    '''