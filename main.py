import time
import random
from graphics import Canvas

# ==========================================
# CONSTANTS & CONFIGURATION
# ==========================================

CANVAS_WIDTH = 420
CANVAS_HEIGHT = 700
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

CENTER_X = CANVAS_WIDTH // 2  # 210

# Global storage for personal journal entries
JOURNAL_ENTRIES = []

# ==========================================
# VIBRANT & STRESS-RELIEF COLOR PALETTE
# ==========================================

BG_OUTSIDE = "#0F172A"       # Deep calming dark slate backdrop
PHONE_BG = "#F8FAFC"         # Crisp clean paper-white app window
PRIMARY_COLOR = "#4F46E5"    # Vibrant Electric Indigo
SECONDARY_COLOR = "#10B981"  # Mint Green Accent
TEXT_DARK = "#1E293B"        # Slate Dark for readable text
TEXT_MUTED = "#64748B"       # Slate Muted for subtitles
CARD_BG = "#FFFFFF"          # Pure white for cards
CARD_BORDER = "#E2E8F0"      # Light border for cards
ACCENT_PINK = "#F43F5E"      # Soft Rose for warnings/love
ACCENT_BLUE = "#38BDF8"      # Light Sky Blue

# ==========================================
# WINDOW FRAME SETUP
# ==========================================

def draw_app_frame(title_text="MindMate"):
    """Draws the gorgeous smartphone frame and app header."""
    # Outer background
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color=BG_OUTSIDE)
    
    # Phone Container
    canvas.create_rectangle(15, 15, CANVAS_WIDTH - 15, CANVAS_HEIGHT - 15, color=PHONE_BG)
    
    # Header Banner
    canvas.create_rectangle(15, 15, CANVAS_WIDTH - 15, 95, color=PRIMARY_COLOR)
    
    # App Title
    canvas.create_text(CENTER_X, 42, text=title_text, font="Helvetica", point_size=20, bold=True, color="white")
    canvas.create_text(CENTER_X, 70, text="Your Personal Wellness Companion", font="Helvetica", point_size=11, color="#E0E7FF")

def draw_back_button():
    """Draws a standard back navigation button at the bottom of inner screens."""
    btn_y = 620
    canvas.create_rectangle(60, btn_y, CANVAS_WIDTH - 60, btn_y + 40, color="#E2E8F0")
    canvas.create_text(CENTER_X, btn_y + 20, text="← Back to Main Menu", font="Helvetica", point_size=12, bold=True, color=TEXT_DARK)

# ==========================================
# SCREEN 1: MAIN MENU (DASHBOARD)
# ==========================================

def show_main_menu():
    """Displays the interactive main dashboard with all feature cards."""
    canvas.clear()
    draw_app_frame("MindMate")
    
    # Subtitle guide
    canvas.create_text(CENTER_X, 120, text="Select an activity to begin:", font="Helvetica", point_size=13, bold=True, color=TEXT_DARK)
    
    # Menu items configuration: (y_top, title, description, accent_color)
    menu_items = [
        (145, "Validate Feelings", "Check in with your mood & get guidance", "#6366F1"),
        (225, "Water Intake Tracker", "Stay hydrated & track your daily sips", "#0EA5E9"),
        (305, "Anxiety & Breathing Session", "Guided 5-sec breathing cycles to reset", "#10B981"),
        (385, "Personal Venting Journal", "Secure safe space for your thoughts", "#8B5CF6"),
        (465, "Daily Boost & Motivation", "Uplifting words & positive mindset quotes", "#F59E0B"),
        (545, "Study & Wellness Tips", "Practical habits for focus & health", "#EC4899")
    ]
    
    # Draw interactive menu cards
    for y_top, title, subtitle, color in menu_items:
        canvas.create_rectangle(35, y_top, CANVAS_WIDTH - 35, y_top + 65, color=CARD_BG)
        canvas.create_rectangle(35, y_top, 45, y_top + 65, color=color)
        canvas.create_text(60, y_top + 22, text=title, font="Helvetica", point_size=13, bold=True, color=TEXT_DARK)
        canvas.create_text(60, y_top + 45, text=subtitle, font="Helvetica", point_size=10, color=TEXT_MUTED)
    
    canvas.create_text(CENTER_X, 645, text="✨ Built with care for Stanford Code in Place", font="Helvetica", point_size=10, color=TEXT_MUTED)
    
    # Handle clicks
    while True:
        click = canvas.get_next_click()
        if 35 <= click.x <= CANVAS_WIDTH - 35:
            if 145 <= click.y <= 210:
                run_validate_feelings()
                return
            elif 225 <= click.y <= 290:
                run_water_tracker()
                return
            elif 305 <= click.y <= 370:
                run_breathing_session()
                return
            elif 385 <= click.y <= 450:
                run_venting_journal()
                return
            elif 465 <= click.y <= 530:
                run_motivation_screen()
                return
            elif 545 <= click.y <= 610:
                run_wellness_tips()
                return

# ==========================================
# FEATURE 1: VALIDATE FEELINGS
# ==========================================

def run_validate_feelings():
    canvas.clear()
    draw_app_frame("Validate Feelings")
    
    canvas.create_text(CENTER_X, 130, text="How is your heart feeling right now?", font="Helvetica", point_size=13, bold=True, color=TEXT_DARK)
    
    moods = [
        (170, "Positive & High Energy", "#10B981"),
        (245, "Calm & Peaceful", "#38BDF8"),
        (320, "Feeling Low / Blue", "#6366F1"),
        (395, "Stressed & Overwhelmed", "#F43F5E")
    ]
    
    for y, text, color in moods:
        canvas.create_rectangle(40, y, CANVAS_WIDTH - 40, y + 55, color=CARD_BG)
        canvas.create_rectangle(40, y, 52, y + 55, color=color)
        canvas.create_text(70, y + 28, text=text, font="Helvetica", point_size=12, bold=True, color=TEXT_DARK)
        
    canvas.create_text(CENTER_X, 500, text="Click on a mood above to receive guidance.", font="Helvetica", point_size=10, color=TEXT_MUTED)
    draw_back_button()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
            
        if 40 <= click.x <= CANVAS_WIDTH - 40:
            msg = ""
            if 170 <= click.y <= 225:
                msg = "It's wonderful to see you shining! Keep spreading that positive energy."
            elif 245 <= click.y <= 300:
                msg = "Embrace this tranquility. Peace is your natural state of mind."
            elif 320 <= click.y <= 375:
                msg = "It's okay to feel low. Be gentle with yourself today; brighter days are ahead."
            elif 395 <= click.y <= 450:
                msg = "You don't have to carry the whole world today. Take a deep breath. One thing at a time."
                
            if msg:
                canvas.create_rectangle(30, 530, CANVAS_WIDTH - 30, 605, color="#EFF6FF")
                canvas.create_rectangle(30, 530, 36, 605, color=PRIMARY_COLOR)
                canvas.create_text(CENTER_X, 567, text=msg, font="Helvetica", point_size=10, color=TEXT_DARK)

# ==========================================
# FEATURE 2: WATER INTAKE TRACKER
# ==========================================

def run_water_tracker():
    water_count = 0
    
    def redraw_water_screen():
        canvas.clear()
        draw_app_frame("Water Tracker")
        
        canvas.create_text(CENTER_X, 130, text="Stay Hydrated, Stay Focused!", font="Helvetica", point_size=14, bold=True, color=TEXT_DARK)
        
        bottle_x1, bottle_y1, bottle_x2, bottle_y2 = 160, 180, 260, 420
        canvas.create_rectangle(bottle_x1, bottle_y1, bottle_x2, bottle_y2, color="#E2E8F0")
        
        fill_ratio = min(water_count / 8.0, 1.0)
        fill_height = int((bottle_y2 - bottle_y1) * fill_ratio)
        if fill_height > 0:
            canvas.create_rectangle(bottle_x1, bottle_y2 - fill_height, bottle_x2, bottle_y2, color="#0EA5E9")
            
        canvas.create_text(CENTER_X, 450, text=f"Glasses Completed: {water_count} / 8", font="Helvetica", point_size=14, bold=True, color=TEXT_DARK)
        
        canvas.create_rectangle(60, 490, CANVAS_WIDTH - 60, 545, color=PRIMARY_COLOR)
        canvas.create_text(CENTER_X, 517, text="🥤 Drink Water (Sip Complete)", font="Helvetica", point_size=12, bold=True, color="white")
        
        if water_count > 0:
            canvas.create_text(CENTER_X, 575, text="Fantastic hydration! Your brain power just leveled up.", font="Helvetica", point_size=10, color=SECONDARY_COLOR)
            
        draw_back_button()

    redraw_water_screen()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
        elif 60 <= click.x <= CANVAS_WIDTH - 60 and 490 <= click.y <= 545:
            water_count += 1
            redraw_water_screen()

# ==========================================
# FEATURE 3: ANXIETY & BREATHING SESSION
# ==========================================

def run_breathing_session():
    canvas.clear()
    draw_app_frame("Anxiety & Breathing")
    
    canvas.create_text(CENTER_X, 130, text="Find Your Center", font="Helvetica", point_size=15, bold=True, color=TEXT_DARK)
    canvas.create_text(CENTER_X, 160, text="Click start below to begin your guided 5-second breathing cycle.", font="Helvetica", point_size=10, color=TEXT_MUTED)
    
    canvas.create_oval(CENTER_X - 80, 220, CENTER_X + 80, 380, color="#E0E7FF")
    canvas.create_text(CENTER_X, 300, text="Breathe", font="Helvetica", point_size=14, bold=True, color=PRIMARY_COLOR)
    
    canvas.create_rectangle(60, 480, CANVAS_WIDTH - 60, 540, color=SECONDARY_COLOR)
    canvas.create_text(CENTER_X, 510, text="🌿 Start Breathing Cycle", font="Helvetica", point_size=13, bold=True, color="white")
    
    draw_back_button()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
            
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 480 <= click.y <= 540:
            canvas.create_rectangle(30, 420, CANVAS_WIDTH - 30, 460, color=PHONE_BG)
            canvas.create_text(CENTER_X, 440, text="Breathe IN slowly... (Expand)", font="Helvetica", point_size=12, bold=True, color=SECONDARY_COLOR)
            time.sleep(2.5)
            
            canvas.create_rectangle(30, 420, CANVAS_WIDTH - 30, 460, color=PHONE_BG)
            canvas.create_text(CENTER_X, 440, text="Hold your breath gently...", font="Helvetica", point_size=12, bold=True, color=PRIMARY_COLOR)
            time.sleep(1.5)
            
            canvas.create_rectangle(30, 420, CANVAS_WIDTH - 30, 460, color=PHONE_BG)
            canvas.create_text(CENTER_X, 440, text="Breathe OUT and release tension...", font="Helvetica", point_size=12, bold=True, color=ACCENT_PINK)
            time.sleep(2.5)
            
            canvas.create_rectangle(30, 420, CANVAS_WIDTH - 30, 460, color=PHONE_BG)
            canvas.create_text(CENTER_X, 440, text="✨ Wonderful! Notice how your body feels lighter.", font="Helvetica", point_size=11, bold=True, color=TEXT_DARK)

# ==========================================
# FEATURE 4: PERSONAL VENTING JOURNAL
# ==========================================

def run_venting_journal():
    canvas.clear()
    draw_app_frame("Safe Venting Journal")
    
    canvas.create_text(CENTER_X, 130, text="Your Private Emotional Vault", font="Helvetica", point_size=14, bold=True, color=TEXT_DARK)
    canvas.create_text(CENTER_X, 155, text="Type your thoughts safely in the terminal prompt.", font="Helvetica", point_size=10, color=TEXT_MUTED)
    
    canvas.create_rectangle(35, 195, CANVAS_WIDTH - 35, 310, color=CARD_BG)
    canvas.create_text(CENTER_X, 235, text="🔒 Confidential & Secure Space", font="Helvetica", point_size=12, bold=True, color=PRIMARY_COLOR)
    canvas.create_text(CENTER_X, 270, text="Check your Python IDE terminal to type out\nand save new thoughts securely.", font="Helvetica", point_size=10, color=TEXT_DARK)
    
    canvas.create_rectangle(60, 360, CANVAS_WIDTH - 60, 420, color=PRIMARY_COLOR)
    canvas.create_text(CENTER_X, 390, text="📖 View Saved Entries Vault", font="Helvetica", point_size=12, bold=True, color="white")
    
    canvas.create_rectangle(60, 440, CANVAS_WIDTH - 60, 500, color=SECONDARY_COLOR)
    canvas.create_text(CENTER_X, 470, text="✏️ Add New Entry (Terminal)", font="Helvetica", point_size=12, bold=True, color="white")
    
    draw_back_button()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
            
        elif 60 <= click.x <= CANVAS_WIDTH - 60 and 440 <= click.y <= 500:
            print("\n--- MINDMATE SECURE JOURNAL TERMINAL ---")
            user_text = input("Type your feelings and emotions here: ")
            if user_text.strip():
                JOURNAL_ENTRIES.append(user_text)
                print("-> Success! Entry saved securely to your personal vault.")
                canvas.create_rectangle(30, 530, CANVAS_WIDTH - 30, 580, color="#DCFCE7")
                canvas.create_text(CENTER_X, 555, text="✅ Entry saved successfully!", font="Helvetica", point_size=11, bold=True, color=SECONDARY_COLOR)
            else:
                print("-> Entry was empty. Nothing saved.")
                
        elif 60 <= click.x <= CANVAS_WIDTH - 60 and 360 <= click.y <= 420:
            canvas.clear()
            draw_app_frame("Journal Vault")
            canvas.create_text(CENTER_X, 130, text=f"Total Saved Entries: {len(JOURNAL_ENTRIES)}", font="Helvetica", point_size=13, bold=True, color=TEXT_DARK)
            
            y_offset = 170
            if not JOURNAL_ENTRIES:
                canvas.create_text(CENTER_X, 300, text="No journal entries yet.\nUse the terminal to add your first reflection!", font="Helvetica", point_size=11, color=TEXT_MUTED)
            else:
                for idx, entry in enumerate(JOURNAL_ENTRIES[-4:], 1):
                    canvas.create_rectangle(30, y_offset, CANVAS_WIDTH - 30, y_offset + 85, color=CARD_BG)
                    canvas.create_text(50, y_offset + 20, text=f"Entry #{idx}:", font="Helvetica", point_size=10, bold=True, color=PRIMARY_COLOR)
                    display_text = entry if len(entry) < 45 else entry[:42] + "..."
                    canvas.create_text(50, y_offset + 50, text=display_text, font="Helvetica", point_size=10, color=TEXT_DARK)
                    y_offset += 100
                    
            draw_back_button()
            while True:
                vault_click = canvas.get_next_click()
                if 60 <= vault_click.x <= CANVAS_WIDTH - 60 and 620 <= vault_click.y <= 660:
                    run_venting_journal()
                    return

# ==========================================
# FEATURE 5: DAILY BOOST & MOTIVATION
# ==========================================

def run_motivation_screen():
    quotes = [
        "“You are stronger than you think.”",
        "“Just let go and trust the process.”",
        "“You don't have to control everything.”",
        "“You bring so much wonderful light and warmth to the world.”",
        "“Every single small step forward is progress.”"
    ]
    
    current_quote = random.choice(quotes)
    
    def redraw_motivation():
        canvas.clear()
        draw_app_frame("Daily Boost")
        
        canvas.create_text(CENTER_X, 130, text="Words of Encouragement", font="Helvetica", point_size=14, bold=True, color=TEXT_DARK)
        
        canvas.create_rectangle(30, 180, CANVAS_WIDTH - 30, 380, color=CARD_BG)
        canvas.create_rectangle(30, 180, CANVAS_WIDTH - 30, 192, color="#F59E0B")
        canvas.create_text(CENTER_X, 280, text=current_quote, font="Helvetica", point_size=13, bold=True, color=TEXT_DARK)
        
        canvas.create_rectangle(60, 440, CANVAS_WIDTH - 60, 500, color="#F59E0B")
        canvas.create_text(CENTER_X, 470, text="✨ Give Me Another Quote", font="Helvetica", point_size=12, bold=True, color="white")
        
        draw_back_button()

    redraw_motivation()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
        elif 60 <= click.x <= CANVAS_WIDTH - 60 and 440 <= click.y <= 500:
            current_quote = random.choice(quotes)
            redraw_motivation()

# ==========================================
# FEATURE 6: STUDY & WELLNESS TIPS
# ==========================================

def run_wellness_tips():
    tips = [
        "Mindset Tip: Remind yourself that mistakes help your brain grow.",
        "Health Tip: Rest your eyes—look away from screens every 20 minutes.",
        "Study Tip: Break large chapters into smaller blocks to avoid burnout.",
        "Habit Tip: Name one good thing that happened to you today.",
        "Sleep Tip: Keep your phone away 30 minutes before bedtime."
    ]
    
    current_tip = random.choice(tips)
    
    def redraw_tips():
        canvas.clear()
        draw_app_frame("Study & Wellness")
        
        canvas.create_text(CENTER_X, 130, text="Wisdom & Habits", font="Helvetica", point_size=14, bold=True, color=TEXT_DARK)
        
        canvas.create_rectangle(30, 180, CANVAS_WIDTH - 30, 380, color=CARD_BG)
        canvas.create_rectangle(30, 180, CANVAS_WIDTH - 30, 192, color=ACCENT_PINK)
        canvas.create_text(CENTER_X, 280, text=current_tip, font="Helvetica", point_size=12, bold=True, color=TEXT_DARK)
        
        canvas.create_rectangle(60, 440, CANVAS_WIDTH - 60, 500, color=ACCENT_PINK)
        canvas.create_text(CENTER_X, 470, text="💡 Get Another Tip", font="Helvetica", point_size=12, bold=True, color="white")
        
        draw_back_button()

    redraw_tips()
    
    while True:
        click = canvas.get_next_click()
        if 60 <= click.x <= CANVAS_WIDTH - 60 and 620 <= click.y <= 660:
            show_main_menu()
            return
        elif 60 <= click.x <= CANVAS_WIDTH - 60 and 440 <= click.y <= 500:
            current_tip = random.choice(tips)
            redraw_tips()

# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

def main():
    show_main_menu()

if __name__ == '__main__':
    main()
