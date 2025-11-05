"""
NEXUS: PREMIUM GUI VERSION
The most beautiful interface for your Data Structures project
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from tkinter import font as tkFont
from data_structures import *
import threading
import time

class NexusGUIPremium:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NEXUS: Multiverse Truth or Dare")
        self.window.geometry("1400x900")
        self.window.configure(bg="#0a0a0a")
        
        # Game state
        self.blockchain = Blockchain()
        self.multiverse = MultiverseGraph()
        self.turn_queue = TurnQueue()
        self.player_map = HashMap()
        self.current_universe = "PRIME"
        self.turn = 0
        
        self.create_styles()
        self.create_widgets()
    
    def create_styles(self):
        """Create professional color scheme"""
        self.colors = {
            "bg_dark": "#0a0a0a",
            "bg_panel": "#1a1a2e",
            "bg_input": "#16213e",
            "border_cyan": "#00ffff",
            "border_magenta": "#ff00ff",
            "text_white": "#ffffff",
            "text_cyan": "#00ffff",
            "text_magenta": "#ff00ff",
            "text_green": "#00ff00",
            "button_cyan": "#00cccc",
            "button_magenta": "#cc00cc"
        }
        
        self.fonts = {
            "title": ("Arial", 24, "bold"),
            "heading": ("Arial", 14, "bold"),
            "normal": ("Arial", 11),
            "small": ("Arial", 9),
            "mono": ("Courier New", 10)
        }
    
    def create_widgets(self):
        """Create UI layout"""
        # ========== HEADER ==========
        header = tk.Frame(self.window, bg=self.colors["bg_panel"], height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)
        
        title_label = tk.Label(
            header,
            text="🌌 NEXUS: MULTIVERSE TRUTH OR DARE 🌌",
            font=self.fonts["title"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_cyan"]
        )
        title_label.pack(pady=10)
        
        subtitle = tk.Label(
            header,
            text="Data Structures in Action | Blockchain • Tree • Queue • HashMap",
            font=("Arial", 10),
            bg=self.colors["bg_panel"],
            fg=self.colors["text_magenta"]
        )
        subtitle.pack()
        
        # ========== MAIN CONTAINER ==========
        main_container = tk.Frame(self.window, bg=self.colors["bg_dark"])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # LEFT PANEL: Player Management
        left_panel = self.create_left_panel(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
        
        # CENTER PANEL: Game Area
        center_panel = self.create_center_panel(main_container)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # RIGHT PANEL: Blockchain & Multiverse
        right_panel = self.create_right_panel(main_container)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
    
    def create_left_panel(self, parent):
        """Left panel: Player management"""
        panel = tk.Frame(parent, bg=self.colors["bg_panel"], width=250)
        panel.pack_propagate(False)
        
        # Title
        title = tk.Label(
            panel,
            text="👥 PLAYERS",
            font=self.fonts["heading"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_cyan"]
        )
        title.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(panel, bg=self.colors["bg_panel"])
        input_frame.pack(padx=10, pady=5, fill=tk.X)
        
        tk.Label(
            input_frame,
            text="Add Player:",
            font=self.fonts["small"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_white"]
        ).pack()
        
        self.player_input = tk.Entry(
            input_frame,
            font=self.fonts["normal"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"],
            insertbackground=self.colors["text_cyan"]
        )
        self.player_input.pack(fill=tk.X, pady=5)
        self.player_input.bind('<Return>', lambda e: self.add_player_gui())
        
        add_btn = tk.Button(
            input_frame,
            text="➕ Add Player",
            font=self.fonts["small"],
            bg=self.colors["button_cyan"],
            fg="#000",
            command=self.add_player_gui,
            relief=tk.FLAT,
            cursor="hand2"
        )
        add_btn.pack(fill=tk.X, pady=5)
        
        # Players list
        tk.Label(
            panel,
            text="Queue Order:",
            font=self.fonts["small"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_magenta"]
        ).pack(padx=10, pady=(10, 5))
        
        self.players_listbox = tk.Listbox(
            panel,
            font=self.fonts["small"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_green"],
            height=8,
            relief=tk.FLAT,
            bd=2,
            highlightcolor=self.colors["border_cyan"]
        )
        self.players_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Stats
        tk.Label(
            panel,
            text="📊 Stats:",
            font=self.fonts["small"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_cyan"]
        ).pack(padx=10, pady=(10, 5))
        
        self.stats_frame = tk.Frame(panel, bg=self.colors["bg_input"])
        self.stats_frame.pack(padx=10, pady=5, fill=tk.X)
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Turn: 0\nBlocks: 1\nUniverses: 1",
            font=self.fonts["small"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_green"],
            justify=tk.LEFT
        )
        self.stats_label.pack(padx=5, pady=5)
        
        return panel
    
    def create_center_panel(self, parent):
        """Center panel: Game area"""
        panel = tk.Frame(parent, bg=self.colors["bg_panel"])
        
        # Challenge display
        self.challenge_frame = tk.Frame(panel, bg=self.colors["bg_input"])
        self.challenge_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.challenge_label = tk.Label(
            self.challenge_frame,
            text="🎮 CHOOSE YOUR FATE",
            font=self.fonts["heading"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"],
            wraplength=400
        )
        self.challenge_label.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.challenge_frame, bg=self.colors["bg_input"])
        button_frame.pack(pady=20)
        
        self.truth_btn = tk.Button(
            button_frame,
            text="🔮 TRUTH",
            font=self.fonts["heading"],
            bg=self.colors["button_cyan"],
            fg="#000",
            width=15,
            height=3,
            command=lambda: self.play_turn("TRUTH"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.truth_btn.pack(side=tk.LEFT, padx=10)
        
        self.dare_btn = tk.Button(
            button_frame,
            text="⚡ DARE",
            font=self.fonts["heading"],
            bg=self.colors["button_magenta"],
            fg=self.colors["text_white"],
            width=15,
            height=3,
            command=lambda: self.play_turn("DARE"),
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.dare_btn.pack(side=tk.LEFT, padx=10)
        
        # Output area
        self.output = scrolledtext.ScrolledText(
            panel,
            font=self.fonts["mono"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_green"],
            height=15,
            relief=tk.FLAT,
            bd=2
        )
        self.output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Configure tags
        self.output.tag_configure("mining", foreground="#ffff00")
        self.output.tag_configure("success", foreground="#00ff00")
        self.output.tag_configure("info", foreground="#00ffff")
        
        return panel
    
    def create_right_panel(self, parent):
        """Right panel: Blockchain & Multiverse"""
        panel = tk.Frame(parent, bg=self.colors["bg_panel"], width=300)
        panel.pack_propagate(False)
        
        # Tabs
        notebook = ttk.Notebook(panel, style="TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab 1: Blockchain
        blockchain_frame = tk.Frame(notebook, bg=self.colors["bg_input"])
        notebook.add(blockchain_frame, text="⛓️  Blockchain")
        
        tk.Label(
            blockchain_frame,
            text="BLOCKS MINED",
            font=self.fonts["small"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"]
        ).pack(pady=5)
        
        self.blockchain_display = scrolledtext.ScrolledText(
            blockchain_frame,
            font=self.fonts["small"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_green"],
            height=20,
            relief=tk.FLAT
        )
        self.blockchain_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Tab 2: Multiverse
        multiverse_frame = tk.Frame(notebook, bg=self.colors["bg_input"])
        notebook.add(multiverse_frame, text="🌌 Multiverse")
        
        tk.Label(
            multiverse_frame,
            text="UNIVERSES (BFS)",
            font=self.fonts["small"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"]
        ).pack(pady=5)
        
        self.multiverse_display = scrolledtext.ScrolledText(
            multiverse_frame,
            font=self.fonts["small"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_magenta"],
            height=20,
            relief=tk.FLAT
        )
        self.multiverse_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Tab 3: Info
        info_frame = tk.Frame(notebook, bg=self.colors["bg_input"])
        notebook.add(info_frame, text="ℹ️  Info")
        
        info_text = tk.Label(
            info_frame,
            text="""DATA STRUCTURES:

1. LINKED LIST (Blockchain)
   • Blocks linked via hash
   • O(2^difficulty) mining
   
2. N-ARY TREE (Multiverse)
   • Multiple children per node
   • O(V+E) BFS traversal
   
3. CIRCULAR QUEUE (Turns)
   • FIFO with wraparound
   • O(1) operations
   
4. HASH MAP (Players)
   • Hash function distribution
   • O(1) average lookup""",
            font=self.fonts["small"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"],
            justify=tk.LEFT
        )
        info_text.pack(padx=10, pady=10)
        
        return panel
    
    def add_player_gui(self):
        """Add player from GUI"""
        name = self.player_input.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Enter player name!")
            return
        
        player = Player(name)
        self.player_map.set(name, player)
        self.turn_queue.enqueue(player)
        
        self.output.insert(tk.END, f"✅ {name} joined the game!\n", "success")
        self.output.see(tk.END)
        
        self.player_input.delete(0, tk.END)
        self.update_display()
    
    def play_turn(self, ctype: str):
        """Play a turn"""
        player = self.turn_queue.peek()
        if not player:
            messagebox.showwarning("No Players", "Add players first!")
            return
        
        challenge = get_random_challenge(ctype)
        
        # Show challenge
        self.challenge_label.config(
            text=f"{ctype}\n\n{challenge}",
            fg=self.colors["text_magenta"] if ctype == "DARE" else self.colors["text_cyan"]
        )
        
        # Ask for response
        response_window = tk.Toplevel(self.window)
        response_window.title("Your Response")
        response_window.geometry("400x200")
        response_window.configure(bg=self.colors["bg_panel"])
        
        tk.Label(
            response_window,
            text=f"{player.name}, enter your response:",
            font=self.fonts["normal"],
            bg=self.colors["bg_panel"],
            fg=self.colors["text_white"]
        ).pack(pady=10)
        
        response_entry = tk.Text(
            response_window,
            font=self.fonts["normal"],
            bg=self.colors["bg_input"],
            fg=self.colors["text_cyan"],
            height=4
        )
        response_entry.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        def submit_response():
            response = response_entry.get("1.0", tk.END).strip()
            
            # Mine block
            self.output.insert(tk.END, "\n⛏️  MINING BLOCK...\n", "mining")
            self.output.see(tk.END)
            self.window.update()
            
            data = {
                "player": player.name,
                "type": ctype,
                "challenge": challenge,
                "response": response
            }
            
            self.blockchain.add_block(data)
            
            # Create universe
            universe_name = f"{player.name}'s {ctype} Reality"
            self.multiverse.create_universe(self.current_universe, universe_name)
            
            # Update
            player.score += 10
            self.turn += 1
            
            self.output.insert(tk.END, f"✅ BLOCK MINED! {player.name} +10 points!\n", "success")
            self.output.insert(tk.END, f"🌌 Universe created: {universe_name}\n", "info")
            
            self.turn_queue.next_turn()
            
            response_window.destroy()
            self.update_display()
        
        tk.Button(
            response_window,
            text="✅ COMPLETE",
            font=self.fonts["normal"],
            bg=self.colors["button_cyan"],
            fg="#000",
            command=submit_response
        ).pack(pady=10)
    
    def update_display(self):
        """Update all displays"""
        # Update players list
        self.players_listbox.delete(0, tk.END)
        for i in range(self.turn_queue.size):
            idx = (self.turn_queue.front + i) % self.turn_queue.capacity
            if self.turn_queue.queue[idx]:
                player = self.turn_queue.queue[idx]
                self.players_listbox.insert(tk.END, f"  {i+1}. {player.name} ({player.score}pts)")
        
        # Update stats
        stats_text = f"Turn: {self.turn}\nBlocks: {len(self.blockchain.chain)}\nUniverses: {len(self.multiverse.nodes)}"
        self.stats_label.config(text=stats_text)
        
        # Update blockchain display
        self.blockchain_display.delete("1.0", tk.END)
        for block in self.blockchain.chain:
            self.blockchain_display.insert(tk.END, f"Block #{block.index}\n")
            self.blockchain_display.insert(tk.END, f"  Player: {block.data.get('player')}\n")
            self.blockchain_display.insert(tk.END, f"  Type: {block.data.get('type')}\n")
            self.blockchain_display.insert(tk.END, f"  Hash: {block.hash[:20]}...\n\n")
        
        # Update multiverse display
        self.multiverse_display.delete("1.0", tk.END)
        for node in self.multiverse.bfs():
            self.multiverse_display.insert(tk.END, f"• {node.name}\n")
    
    def run(self):
        """Run GUI"""
        self.update_display()
        self.window.mainloop()

if __name__ == "__main__":
    app = NexusGUIPremium()
    app.run()
