import time
import random
from graphics import Canvas


 ==================================================

CANVAS_WIDTH = 420
CANVAS_HEIGHT = 700
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

CENTER_X = CANVAS_WIDTH // 2  # 210

# Global storage for personal journal entries
JOURNAL_ENTRIES = []

# ==================================================
# VIBRANT & STRESS-RELIEF COLOR PALETTE
# ==================================================
BG_OUTSIDE = "#0F172A"       # Deep calming dark slate backdrop
PHONE_BG = "#F8FAFC"         # Crisp clean paper-white app window
PRIMARY_COLOR = "#4F46E5"    # Vibrant Electric Indigo
ACCENT_TEAL = "#0D9488"      # Refreshing medical teal
BUBBLE_BOT = "#EEF2FF"       # Soft indigo card container
BUBBLE_USER = "#E0E7FF"      # User highlight bubble
TEXT_DARK = "#1E1B4B"        # Heavy bold dark navy for readability
TEXT_MUTED = "#64748B"       # Secondary slate
WHITE = "#FFFFFF"

def draw_phone_frame(title="MindMate"):
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, BG_OUTSIDE)
    canvas.create_rectangle(15, 15, CANVAS_WIDTH - 15, CANVAS_HEIGHT - 15, PHONE_BG)
    canvas.create_rectangle(15, 15, CANVAS_WIDTH - 15, 80, PRIMARY_COLOR)
    
    canvas.create_text(45, 47, "‹", "Helvetica 22 bold", WHITE)
    canvas.create_text(CENTER_X, 47, title, "Helvetica 15 bold", WHITE)
    canvas.create_text(CANVAS_WIDTH - 45, 47, "≡", "Helvetica 18 bold", WHITE)
    
    canvas.create_text(CENTER_X, CANVAS_HEIGHT - 25, "Created by Safiya Pathan", "Helvetica 9 bold italic", TEXT_MUTED)

def draw_bottom_input_bar():
    bar_y = CANVAS_HEIGHT - 65
    canvas.create_rectangle(25, bar_y, CANVAS_WIDTH - 25, bar_y + 40, WHITE)
    canvas.create_rectangle(25, bar_y, CANVAS_WIDTH - 25, bar_y + 40, "#CBD5E1")
    canvas.create_text(50, bar_y + 20, "🔍", "Helvetica 12", TEXT_MUTED)
    canvas.create_text(85, bar_y + 20, "Talk to MindMate...", "Helvetica 11 bold", TEXT_DARK)
    canvas.create_oval(CANVAS_WIDTH - 55, bar_y + 5, CANVAS_WIDTH - 31, bar_y + 35, PRIMARY_COLOR)
    canvas.create_text(CANVAS_WIDTH - 43, bar_y + 20, "✨", "Helvetica 11", WHITE)

def draw_bot_avatar(x, y):
    canvas.create_oval(x - 22, y - 22, x + 22, y + 22, PRIMARY_COLOR)
    canvas.create_text(x, y, "🧠", "Helvetica 18", WHITE)

# ==================================================
# WELCOME / HOME SCREEN
# ==================================================

def welcome_screen():
    canvas.clear()
    draw_phone_frame("MindMate")
    
    draw_bot_avatar(CENTER_X, 115)
    canvas.create_text(CENTER_X, 152, "Hey there, Friend! 💙", "Helvetica 16 bold", TEXT_DARK)
    canvas.create_text(CENTER_X, 173, "I'm your personalized wellness companion", "Helvetica 11 bold", TEXT_MUTED)
    
    options = [
        "😊  Validate Feelings",
        "🥤  Water Intake Tracker",
        "🌿  Anxiety & Breathing Session",
        "📓  Personal Venting & Safe Journal",
        "⭐  Daily Boost & Motivation",
        "📚  Study & Wellness Tips",
        "🎮  Mini-Games Hub (Quizzes, Dice, Coin)"
    ]
    
    start_y = 195
    for i, opt in enumerate(options):
        by = start_y + (i * 42)
        canvas.create_rectangle(30, by, CANVAS_WIDTH - 30, by + 36, BUBBLE_BOT)
        canvas.create_rectangle(30, by, CANVAS_WIDTH - 30, by + 36, "#C7D2FE")
        canvas.create_text(50, by + 18, opt, "Helvetica 11 bold", TEXT_DARK)

    while True:
        canvas.wait_for_click()
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 30 <= x <= CANVAS_WIDTH - 30:
            if 195 <= y <= 231: chat_mood(); return
            elif 237 <= y <= 273: chat_water(); return
            elif 279 <= y <= 315: chat_breathing(); return
            elif 321 <= y <= 357: journal_home(); return
            elif 363 <= y <= 399: chat_motivation(); return
            elif 405 <= y <= 441: chat_tips(); return
            elif 447 <= y <= 483: chat_minigames_hub(); return

def render_chat_layout(bot_msg_line1, bot_msg_line2=""):
    canvas.clear()
    draw_phone_frame("MindMate Chat")
    
    draw_bot_avatar(50, 115)
    canvas.create_text(85, 105, "MindMate", "Helvetica 10 bold", PRIMARY_COLOR)
    
    canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 200, BUBBLE_BOT)
    canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 200, "#CBD5E1")
    
    canvas.create_text(90, 143, bot_msg_line1, "Helvetica 11 bold", TEXT_DARK)
    if bot_msg_line2:
        canvas.create_text(90, 168, bot_msg_line2, "Helvetica 11 bold", TEXT_DARK)
        
    draw_bottom_input_bar()

def handle_back_clicks():
    x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
    if (20 <= x <= 70 and 25 <= y <= 75) or (CANVAS_HEIGHT - 65 <= y <= CANVAS_HEIGHT - 25):
        welcome_screen()
        return True
    return False

# ==================================================
# PERSONAL VENTING & SAFE JOURNAL MODULE
# ==================================================

def journal_home():
    canvas.clear()
    draw_phone_frame("Safe Venting Journal")
    
    draw_bot_avatar(CENTER_X, 125)
    canvas.create_text(CENTER_X, 168, "Your Private Safe Space 📓", "Helvetica 16 bold", TEXT_DARK)
    canvas.create_text(CENTER_X, 190, "Venture your thoughts safely", "Helvetica 11 bold", TEXT_MUTED)
    canvas.create_text(CENTER_X, 202, "Start writing in the terminal provided below", "Helvetica 16 bold", TEXT_DARK)
    
    actions = [
        "✍️  Open Diary (Type with Keyboard)",
        "📖  View Saved Personal Entries",
        "🔒  Lock & Return to Home"
    ]
    
    start_y = 230
    for i, act in enumerate(actions):
        by = start_y + (i * 60)
        canvas.create_rectangle(35, by, CANVAS_WIDTH - 35, by + 48, BUBBLE_BOT)
        canvas.create_rectangle(35, by, CANVAS_WIDTH - 35, by + 48, "#818CF8")
        canvas.create_text(CENTER_X, by + 24, act, "Helvetica 12 bold", TEXT_DARK)
        
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 35 <= x <= CANVAS_WIDTH - 35:
            if 230 <= y <= 278: journal_keyboard_input(); return
            elif 290 <= y <= 338: journal_view_entries(); return
            elif 350 <= y <= 398: welcome_screen(); return

def journal_keyboard_input():
    canvas.clear()
    draw_phone_frame("Open Diary Journal")
    
    canvas.create_text(CENTER_X, 115, "Write Your Feelings & Emotions 📖", "Helvetica 13 bold", PRIMARY_COLOR)
    canvas.create_text(CENTER_X, 138, "Please look at your terminal keyboard", "Helvetica 10 bold", TEXT_MUTED)
    canvas.create_text(CENTER_X, 155, "Start venting", "Helvetica 10 bold", TEXT_MUTED)
    canvas.create_text(CENTER_X, 175, "to exit click ENTER in terminal", "Helvetica 10 bold", TEXT_MUTED)
    
    # Direct keyboard diary opening prompt
    custom_text = input("\n📝 [MindMate Diary] Type your feelings and emotions here: ")
    
    if custom_text.strip() != "":
        JOURNAL_ENTRIES.append(custom_text)
        
    journal_success_screen()

def journal_success_screen():
    canvas.clear()
    draw_phone_frame("Journal Saved")
    
    draw_bot_avatar(CENTER_X, 150)
    canvas.create_text(CENTER_X, 200, "Welcome to yourprivate journal! 🔒", "Helvetica 13 bold", TEXT_DARK)
    canvas.create_text(CENTER_X, 230, "Your emotions are valid and safe here.", "Helvetica 11 bold", TEXT_MUTED)
    
    btn_y = 300
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 50, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 25, "📖 View Saved Journal", "Helvetica 12 bold", WHITE)
    
    home_y = 365
    canvas.create_rectangle(45, home_y, CANVAS_WIDTH - 45, home_y + 50, ACCENT_TEAL)
    canvas.create_text(CENTER_X, home_y + 25, "🏠 Back to Safe Journal Hub", "Helvetica 12 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45:
            if btn_y <= y <= btn_y + 50: journal_view_entries(); return
            elif home_y <= y <= home_y + 50: journal_home(); return

def journal_view_entries():
    canvas.clear()
    draw_phone_frame("Private Journal Entries")
    
    canvas.create_text(CENTER_X, 105, "Your Personal Venting Vault 🔒", "Helvetica 14 bold", PRIMARY_COLOR)
    
    y_offset = 135
    if len(JOURNAL_ENTRIES) == 0:
        canvas.create_rectangle(30, y_offset, CANVAS_WIDTH - 30, y_offset + 60, BUBBLE_BOT)
        canvas.create_text(CENTER_X, y_offset + 30, "Your vault is currently empty.", "Helvetica 11 bold", TEXT_MUTED)
    else:
        for i, entry in enumerate(JOURNAL_ENTRIES[-4:]):
            box_y = y_offset + (i * 75)
            canvas.create_rectangle(30, box_y, CANVAS_WIDTH - 30, box_y + 65, BUBBLE_BOT)
            canvas.create_rectangle(30, box_y, CANVAS_WIDTH - 30, box_y + 65, "#CBD5E1")
            canvas.create_text(45, box_y + 20, f"Entry #{len(JOURNAL_ENTRIES) - 3 + i if len(JOURNAL_ENTRIES) >= 4 else i + 1}", "Helvetica 10 bold", PRIMARY_COLOR)
            canvas.create_text(45, box_y + 42, entry, "Helvetica 10 bold", TEXT_DARK)
            
    btn_y = CANVAS_HEIGHT - 80
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 45, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 22, "🏠 Back to Safe Journal Hub", "Helvetica 11 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 45:
            journal_home()
            return

# ==================================================
# OTHER MODULES (MOOD, WATER, BREATHING, TIPS, GAMES)
# ==================================================

def chat_mood():
    render_chat_layout("How is your heart feeling right now?", "Select your mood below to continue:")
    
    moods = [
        "😊  Positive & High Energy",
        "😌  Calm & Peaceful",
        "😔  Feeling Low / Blue",
        "😰  Stressed & Overwhelmed"
    ]
    
    for i, m in enumerate(moods):
        my = 220 + (i * 52)
        canvas.create_rectangle(30, my, CANVAS_WIDTH - 30, my + 44, BUBBLE_USER)
        canvas.create_rectangle(30, my, CANVAS_WIDTH - 30, my + 44, "#818CF8")
        canvas.create_text(50, my + 22, m, "Helvetica 11 bold", TEXT_DARK)
        
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 30 <= x <= CANVAS_WIDTH - 30:
            if 220 <= y <= 264:
                responses = [
                    "Your radiance is contagious! Keep shining brightly today.",
                    "Love this high frequency! Channel this great energy into your goals.",
                    "Fantastic! Take a moment to appreciate how far you've come."
                ]
                response_screen(random.choice(responses))
            elif 272 <= y <= 316:
                responses = [
                    "Breathe in that lovely peace and let it anchor your soul.",
                    "Tranquility is your superpower. Enjoy this quiet strength.",
                    "A calm mind clears the path for wonderful new ideas."
                ]
                response_screen(random.choice(responses))
            elif 324 <= y <= 368:
                responses = [
                    "I am right here holding space for you.",
                    "It's completely okay to have heavy days. ",
                    "Allow yourself to rest without guilt. U matter a lot!"
                ]
                response_screen(random.choice(responses))
            elif 376 <= y <= 420:
                responses = [
                    "Let's pause right now. Drop your shoulders and take a slow breath.",
                    "You don't have to carry the whole world today. One thing at a time.",
                    "Pause, breathe, and reset. You are completely safe in this moment."
                ]
                response_screen(random.choice(responses))
            return

def chat_water():
    render_chat_layout("Water Intake Tracker: Stay hydrated!", "Click the button below when you finish drinking:")
    
    bx = CENTER_X - 30
    by = 210
    
    canvas.create_rectangle(bx + 18, by, bx + 42, by + 12, PRIMARY_COLOR)
    canvas.create_rectangle(bx + 26, by - 12, bx + 34, by, PRIMARY_COLOR)
    canvas.create_rectangle(bx + 15, by + 12, bx + 45, by + 22, ACCENT_TEAL)
    canvas.create_rectangle(bx, by + 22, bx + 60, by + 130, WHITE)
    canvas.create_rectangle(bx, by + 22, bx + 60, by + 130, "#CBD5E1")
    
    canvas.create_rectangle(bx + 3, by + 40, bx + 57, by + 127, "#0EA5E9")
    
    btn_y = 360
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 45, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 22, "🥤 I Drank Water (Sip Complete)", "Helvetica 11 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 45:
            for level_top in range(by + 40, by + 120, 12):
                canvas.create_rectangle(bx + 3, level_top, bx + 57, by + 127, WHITE)
                time.sleep(0.06)
            
            time.sleep(0.3)
            response_screen("Fantastic hydration! Your brain power and clarity just leveled up.")
            return

def chat_breathing():
    render_chat_layout("Anxiety & Breathing Session", "Settle down. Click start for 5 slow cycles:")
    
    btn_y = 250
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 50, ACCENT_TEAL)
    canvas.create_text(CENTER_X, btn_y + 25, "🌿 Start 5-Cycle Breathing", "Helvetica 12 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 50:
            run_breathing_cycles()
            return

def run_breathing_cycles():
    for cycle in range(1, 6):
        for r in range(25, 75, 12):
            canvas.clear()
            draw_phone_frame(f"Breathing ({cycle}/5)")
            draw_bot_avatar(50, 115)
            canvas.create_text(85, 105, "MindMate ", "Helvetica 10 bold", PRIMARY_COLOR)
            canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 185, BUBBLE_BOT)
            canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 185, "#CBD5E1")
            canvas.create_text(90, 152, f"Cycle {cycle}: Breathe IN (1s)...", "Helvetica 11 bold", TEXT_DARK)
            
            canvas.create_oval(CENTER_X - r, 380 - r, CENTER_X + r, 380 + r, "#CCFBF1")
            canvas.create_oval(CENTER_X - (r//2), 380 - (r//2), CENTER_X + (r//2), 380 + (r//2), ACCENT_TEAL)
            time.sleep(0.75)
            
        time.sleep(0.3)
        
        for r in range(75, 24, -12):
            canvas.clear()
            draw_phone_frame(f"Breathing ({cycle}/5)")
            draw_bot_avatar(50, 115)
            canvas.create_text(85, 105, "MindMate AI", "Helvetica 10 bold", PRIMARY_COLOR)
            canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 185, BUBBLE_BOT)
            canvas.create_rectangle(75, 120, CANVAS_WIDTH - 25, 185, "#CBD5E1")
            canvas.create_text(90, 152, f"Cycle {cycle}: Breathe OUT (1s)...", "Helvetica 11 bold", TEXT_DARK)
            
            canvas.create_oval(CENTER_X - r, 380 - r, CENTER_X + r, 380 + r, "#E2E8F0")
            canvas.create_oval(CENTER_X - (r//2), 380 - (r//2), CENTER_X + (r//2), 380 + (r//2), TEXT_MUTED)
            time.sleep(0.75)

    calming_quotes = [
        "“Peace comes from within. Do not seek it without.”",
        "“You are doing wonderful. Your breath is your anchor.”",
        "“Within you, there is a stillness and a sanctuary.”",
        "“Quiet the mind, and the soul will speak.”"
    ]
    response_screen(random.choice(calming_quotes))

def chat_motivation():
    quotes = [
        "“You don't have to control everything. ”",
        "“Small daily progress adds up to massive life-changing results.”",
        "“Your potential to heal, learn, and grow is completely limitless.”",
        "“You bring so much wonderful light and warmth to the world.”",
        "“Tough times never last, but tough, resilient people do.”",
        "“Just let go and trust the process.”",
        "“You are stronger than you think.”",
        "“Believe in yourself and all that you are. ”"
    ]
    render_chat_layout("Daily Boost & Inspiration:", random.choice(quotes))
    
    btn_y = 250
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 48, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 24, "✨ Give Me Another Quote", "Helvetica 11 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 48:
            chat_motivation()
            return

def chat_tips():
    tips = [
    "📚 Study Tip: Break large chapters into smaller blocks.",
    "🌱 Mindset Tip: Focus only on what you can change right now.",
    "💤 Wellness Tip: Read a physical book before bed.",
    "💡 Focus Tip: Close all unnecessary browser tabs before working.",
    "🍎 Health Tip: Rest ur👀..looking away from screens every 20 mins.",
    "💤 Wellness Tip: Go to bed & wake up at the exact same time daily.",
    "📚 Study Tip: Review yesterday's notes before starting new topics.",
    "🌱 Mindset Tip: Celebrate small wins!",
    "💡 Focus Tip: Put your phone on silent and face-down on your desk.",
    "🍎 Health Tip: Drink a full glass of water right after waking up.",
    "📚 Study Tip: Teach concepts aloud to test your true understanding.",
    "💤 Wellness Tip: Drink a warm cup of caffeine-free chamomile tea.",
    "💡 Focus Tip: Wear noise-canceling headphones",
    "🌱 Mindset Tip: Name one good thing that happened to you today.",
    "🍎 Health Tip: Eat a piece of fresh fruit instead of sugary snacks.",
    "📚 Study Tip: Keep your phone in another room while studying.",
    "💡 Focus Tip: Write down your top three priorities every morning.",
    "💤 Wellness Tip: Keep your bedroom cool and dark for better sleep.",
    "🌱 Mindset Tip: Remind yourself that mistakes help your brain grow.",
    "🍎 Health Tip: Do 10 jumping jacks & boost your morning circulation.",
    "📚 Study Tip: Create flashcards for quick active recall practice.",
    "💡 Focus Tip: Tackle hardest task first while your energy is high.",
    "💤 Wellness Tip: Do a quick gentle body stretch before resting.",
    "🌱 Mindset Tip: Forgive yourself for things outside your control.",
    "🍎 Health Tip: Take deep belly breaths whenever you feel tense."
    ]
    render_chat_layout("Study & Wellness Wisdom:", random.choice(tips))
    
    btn_y = 250
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 48, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 24, "💡 Get Another Tip", "Helvetica 11 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 48:
            chat_tips()
            return

def chat_minigames_hub():
    canvas.clear()
    draw_phone_frame("Mini-Games Hub")
    
    draw_bot_avatar(CENTER_X, 115)
    canvas.create_text(CENTER_X, 155, "Interactive Wellness & Fun Hub", "Helvetica 15 bold", TEXT_DARK)
    canvas.create_text(CENTER_X, 178, "Choose an activity to engage your mind:", "Helvetica 11 bold", TEXT_MUTED)
    
    games = [
        "🍎 Health & Nutrition Quiz",
        "🪙 Flip a Coin (Decision Maker)",
        "🎲 Roll a Dice (Random Choices 1-6)"
    ]
    
    start_y = 210
    for i, g in enumerate(games):
        by = start_y + (i * 60)
        canvas.create_rectangle(35, by, CANVAS_WIDTH - 35, by + 50, BUBBLE_BOT)
        canvas.create_rectangle(35, by, CANVAS_WIDTH - 35, by + 50, "#818CF8")
        canvas.create_text(CENTER_X, by + 25, g, "Helvetica 12 bold", TEXT_DARK)
        
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 35 <= x <= CANVAS_WIDTH - 35:
            if 210 <= y <= 260: game_food_quiz(); return
            elif 270 <= y <= 320: game_coin_flip(); return
            elif 330 <= y <= 380: game_roll_dice(); return

def game_food_quiz():
    question_bank = [
        ("Which option is the healthier choice for your body?", 
         [("🥗 Fresh Green Salad", True), 
          ("🍕 Greasy Pepperoni Pizza", False), 
          ("🥦 Steamed Fresh Vegetables", True), 
          ("🍔 Fast-Food Double Burger", False)]),
        
        ("Which junk food should you avoid eating very often?", 
         [("🍎 Crisp Red Apple", False), 
          ("🥤 Sugary Carbonated Soda", True), 
          ("🥜 Raw Mixed Almonds", False), 
          ("🍟 Deep-Fried French Fries", True)]),

        ("What is the best beverage choice for optimal hydration?", 
         [("💧 Pure Fresh Water", True), 
          ("🧃 High-Sugar Fruit Juice", False), 
          ("⚡ Caffeinated Energy Drink", False), 
          ("🥥 Natural Coconut Water", True)]),

        ("Which snack provides sustained energy for deep study sessions?", 
         [("🍫 Milk Chocolate Bar", False), 
          ("🥜 Walnuts and Blueberries", True), 
          ("🍩 Glazed Sugar Doughnut", False), 
          ("🥣 Instant Potato Chips", False)])
    ]
    
    q_data = random.choice(question_bank)
    q_title = q_data[0]
    choices = q_data[1]
    
    render_chat_layout("Food & Wellness Quiz", q_title)
    
    for i, (opt_text, _) in enumerate(choices):
        oy = 215 + (i * 42)
        canvas.create_rectangle(30, oy, CANVAS_WIDTH - 30, oy + 36, BUBBLE_USER)
        canvas.create_rectangle(30, oy, CANVAS_WIDTH - 30, oy + 36, "#818CF8")
        canvas.create_text(50, oy + 18, opt_text, "Helvetica 11 bold", TEXT_DARK)
        
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 30 <= x <= CANVAS_WIDTH - 30:
            selected_idx = -1
            if 215 <= y <= 251: selected_idx = 0
            elif 257 <= y <= 293: selected_idx = 1
            elif 299 <= y <= 335: selected_idx = 2
            elif 341 <= y <= 377: selected_idx = 3
            
            if selected_idx != -1:
                is_correct = choices[selected_idx][1]
                if is_correct:
                    response_screen("🌟 Brilliant! You accurately identified the healthy wellness choice.")
                else:
                    response_screen("💫 Careful! That option can negatively impact your vitality.")
                return

def game_coin_flip():
    render_chat_layout("Decision Dilemma Coin Flip", "Stuck between two choices? Flip the coin below:")
    
    btn_y = 260
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 50, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 25, "🪙 Tap to Flip Coin", "Helvetica 12 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 50:
            result = random.choice(["HEADS 👑 (Go with Decision A)", "TAILS 🌟 (Go with Decision B)"])
            response_screen(f"Coin Result: {result}")
            return

def game_roll_dice():
    render_chat_layout("Random Choice Dice (1 to 6)", "Have multiple choices? Roll the dice for a random number:")
    
    btn_y = 260
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 50, ACCENT_TEAL)
    canvas.create_text(CENTER_X, btn_y + 25, "🎲 Tap to Roll Dice", "Helvetica 12 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 50:
            roll = random.randint(1, 6)
            response_screen(f"Dice Rolled: 🎲 {roll}! (Option {roll} selected)")
            return

def response_screen(reply_text):
    canvas.clear()
    draw_phone_frame("MindMate")
    
    canvas.create_rectangle(75, 115, CANVAS_WIDTH - 25, 160, BUBBLE_USER)
    canvas.create_rectangle(75, 115, CANVAS_WIDTH - 25, 160, "#CBD5E1")
    canvas.create_text(CENTER_X + 15, 137, "Got it, thanks!", "Helvetica 11 bold", TEXT_DARK)
    
    draw_bot_avatar(50, 205)
    canvas.create_text(85, 185, "MindMate", "Helvetica 10 bold", PRIMARY_COLOR)
    canvas.create_rectangle(75, 200, CANVAS_WIDTH - 25, 295, BUBBLE_BOT)
    canvas.create_rectangle(75, 200, CANVAS_WIDTH - 25, 295, "#CBD5E1")
    canvas.create_text(90, 247, reply_text, "Helvetica 11 bold", TEXT_DARK)
    
    btn_y = 340
    canvas.create_rectangle(45, btn_y, CANVAS_WIDTH - 45, btn_y + 48, PRIMARY_COLOR)
    canvas.create_text(CENTER_X, btn_y + 24, "🏠 Back to Home Chat", "Helvetica 12 bold", WHITE)
    
    while True:
        canvas.wait_for_click()
        if handle_back_clicks(): return
        x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
        if 45 <= x <= CANVAS_WIDTH - 45 and btn_y <= y <= btn_y + 48:
            welcome_screen()
            return

def main():
    welcome_screen()

main()
