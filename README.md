# Peace-Keeper

Mother Base Game System README
Welcome to Mother Base, a small-scale strategic simulation game focused on base construction and mission execution. As the Commander (Boss), you will work alongside your tactical advisor, Freya, to manage resources, build platforms, plan operations, and expand the influence of your private military company (PMC).

Module Overview


1 Base (Base Management Module)
    Handles overall base funds, platform construction, and deployment.

    Initial funds: 5000 credits.

    Available platforms:

    Intelligence Unit

    Medic Unit

    Support Unit

    Development Unit

    Platform benefits: Each platform provides bonuses to specific mission types, increasing success rates.

    Functions:

    Check current funds.

    Build new platforms (requires spending funds).

    Display platform layout in a cross-map format.



2 Task (Mission Module)
    Provides a list of missions and executes them.

    Mission tiers: easy, medium, hard.

    Each mission includes:

    Name and description.

    Success rate (affected by platform bonuses).

    Cost to deploy and potential rewards.

    Outcomes trigger unique situational dialogues, including stealth references, intense firefights, or even some dark humor.

    Functions:

    View mission list.

    Select missions based on type and success rate.

    Earn rewards or face penalties depending on success or failure.



3 Advisor (Tactical Advisor Module)
    Freya, your in-game advisor, offers intelligent tips.

    Provides:

    Recommendations on financial status.

    Suggestions for platform construction.

    Risk assessments and recommendations for missions.

    Emotional and motivational feedback after missions.

    Designed to enhance immersion and deepen player interaction.



4 Main (Main Program Module)
    Central control menu:

    Show base status.

    Show current funds.

    Enter platform construction mode.

    View and execute tasks.

    Ask Freya for advice.

    Exit the game.



To run the game:
    python main.py

 
 
 Gameplay Loop
    1 Start the game; Freya provides an introductory guide.
    2 Check the current status of your base and available funds.
    3 Select and execute missions to accumulate more resources.
    4 Use funds to construct new platforms and improve operational capabilities.
    5 Balance risk and reward with Freya’s guidance.
    6 Continue expanding your Mother Base to become a dominant force in the PMC world
