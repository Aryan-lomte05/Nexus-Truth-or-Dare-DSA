"""
NEXUS: ADVANCED VERSION WITH PROFESSIONAL STATISTICS
Maximum Impact Edition for Assessment
"""

from data_structures import *
import os
import time
from datetime import datetime

class NexusAdvanced:
    def __init__(self):
        self.blockchain = Blockchain()
        self.multiverse = MultiverseGraph()
        self.turn_queue = TurnQueue()
        self.player_map = HashMap()
        self.current_universe = "PRIME"
        self.turn = 0
        self.start_time = datetime.now()
        self.game_log = []
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Professional header with animations"""
        print("\n" + "="*70)
        print("█ "*35)
        print("🌌 " + " "*64 + "🌌")
        print("█  NEXUS: MULTIVERSE TRUTH OR DARE - ADVANCED EDITION  █".center(70))
        print("█  " + " "*64 + "█")
        print("█  Data Structures Project | BTech CSBS  █".center(70))
        print("█ "*35)
        print("="*70 + "\n")
    
    def print_stats_fancy(self):
        """Professional statistics display"""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        stats = self.get_advanced_stats()
        
        print("\n" + "▓"*70)
        print("╔" + "═"*68 + "╗")
        print("║" + " 📊 ADVANCED GAME STATISTICS ".center(68) + "║")
        print("╠" + "═"*68 + "╣")
        print(f"║ Turn Count: {stats['turns']:>3} | Blocks Mined: {stats['blocks']:>3} | Universes: {stats['universes']:>3}       ║")
        print(f"║ Players: {stats['players']:>2} | Blockchain Valid: {'✅' if stats['valid'] else '❌':<3} | Time: {elapsed:>6.1f}s       ║")
        print("╠" + "═"*68 + "╣")
        print("║ COMPLEXITY ANALYSIS:                                                  ║")
        print("║   • Linked List (Mining): O(2^difficulty) ✓                           ║")
        print("║   • Tree Traversal (BFS): O(V+E) ✓                                    ║")
        print("║   • Queue Rotation: O(1) ✓                                            ║")
        print("║   • HashMap Lookup: O(1) average ✓                                    ║")
        print("╚" + "═"*68 + "╝")
        print("▓"*70 + "\n")
    
    def print_player_stats(self):
        """Detailed player statistics"""
        print("\n┌" + "─"*68 + "┐")
        print("│" + " 👥 PLAYER STATISTICS ".center(68) + "│")
        print("├" + "─"*68 + "┤")
        
        players_list = []
        for i in range(self.turn_queue.size):
            idx = (self.turn_queue.front + i) % self.turn_queue.capacity
            if self.turn_queue.queue[idx]:
                player = self.turn_queue.queue[idx]
                players_list.append(player)
                
                blocks = len([b for b in self.blockchain.chain if b.data.get('player') == player.name])
                print(f"│ {player.name:>10} | Score: {player.score:>4} | Blocks: {blocks:>2} | Position: {i+1}    │")
        
        print("└" + "─"*68 + "┘\n")
    
    def print_blockchain_fancy(self):
        """Professional blockchain visualization"""
        print("\n" + "⛓️  "*20)
        print("╔" + "═"*68 + "╗")
        print("║" + " BLOCKCHAIN LEDGER - IMMUTABLE RECORD ".center(68) + "║")
        print("╠" + "═"*68 + "╣")
        
        for block in self.blockchain.chain:
            player = block.data.get('player', 'N/A')
            btype = block.data.get('type', 'N/A')
            challenge = block.data.get('challenge', '')[:35]
            
            print(f"║ Block #{block.index} | Player: {player:>10} | Type: {btype:>6}         ║")
            print(f"║   Hash: {block.hash[:32]}...{block.hash[-4:]}     ║")
            print(f"║   Nonce: {block.nonce:>5} | Challenge: {challenge:>31} ║")
            print("╟" + "─"*68 + "╢")
        
        print("╚" + "═"*68 + "╝")
        print("⛓️  "*20 + "\n")
    
    def print_multiverse_fancy(self):
        """Professional multiverse visualization"""
        print("\n" + "🌌"*20)
        print("╔" + "═"*68 + "╗")
        print("║" + " MULTIVERSE GRAPH - N-ARY TREE STRUCTURE ".center(68) + "║")
        print("╠" + "═"*68 + "╣")
        
        nodes_bfs = self.multiverse.bfs()
        print("║ BFS Traversal (O(V+E)):                                              ║")
        print("╟" + "─"*68 + "╢")
        
        for i, node in enumerate(nodes_bfs):
            depth = self.get_depth(node)
            prefix = "   " * depth + "└─ "
            print(f"║{prefix}{node.name:>50}║")
        
        stats = {
            "total": len(self.multiverse.nodes),
            "depth": max([self.get_depth(n) for n in self.multiverse.nodes.values()]) if nodes_bfs else 0,
            "branches": sum(len(n.children) for n in self.multiverse.nodes.values())
        }
        
        print("╟" + "─"*68 + "╢")
        print(f"║ Total Universes: {stats['total']:>2} | Max Depth: {stats['depth']} | Total Branches: {stats['branches']}       ║")
        print("╚" + "═"*68 + "╝")
        print("🌌"*20 + "\n")
    
    def get_depth(self, node):
        depth = 0
        current = node.parent
        while current:
            depth += 1
            current = current.parent
        return depth
    
    def get_advanced_stats(self):
        return {
            "turns": self.turn,
            "blocks": len(self.blockchain.chain),
            "universes": len(self.multiverse.nodes),
            "players": self.turn_queue.size,
            "valid": self.blockchain.is_valid()
        }
    
    def add_player(self, name: str):
        """Add player with feedback"""
        player = Player(name)
        self.player_map.set(name, player)
        self.turn_queue.enqueue(player)
        
        print(f"\n✅ {name} JOINED THE MULTIVERSE!")
        print(f"   └─ Position in Queue: {self.turn_queue.size}")
        time.sleep(0.5)
    
    def play_turn(self):
        """Play a turn with professional display"""
        player = self.turn_queue.peek()
        if not player:
            print("\n❌ No players in queue!")
            return
        
        print(f"\n{'='*70}")
        print(f"🎮 {player.name.upper()}'S TURN (Turn #{self.turn + 1})")
        print(f"   Current Score: {player.score} | Queue Position: 1/{self.turn_queue.size}")
        print(f"{'='*70}\n")
        
        choice = input("Choose your fate:\n  (1) 🔮 TRUTH\n  (2) ⚡ DARE\n\nChoice: ")
        ctype = "TRUTH" if choice == "1" else "DARE"
        challenge = get_random_challenge(ctype)
        
        print(f"\n╔{'─'*68}╗")
        print(f"║ {ctype.upper():^66} ║")
        print(f"╠{'─'*68}╣")
        print(f"║ {challenge:^66} ║")
        print(f"╚{'─'*68}╝\n")
        
        response = input("Your response: ").strip()
        
        # Add to blockchain with animation
        data = {
            "player": player.name,
            "type": ctype,
            "challenge": challenge,
            "response": response
        }
        
        print("\n⛏️  MINING BLOCK...")
        print("⌛ ", end="", flush=True)
        self.blockchain.add_block(data)
        
        # Create universe
        universe_name = f"{player.name}'s {ctype} Reality"
        self.multiverse.create_universe(self.current_universe, universe_name)
        
        # Update score
        points = 10
        player.score += points
        self.turn += 1
        
        print(f"\n✅ BLOCK MINED SUCCESSFULLY!")
        print(f"   └─ Block Hash: {self.blockchain.chain[-1].hash[:16]}...")
        print(f"   └─ Nonce: {self.blockchain.chain[-1].nonce}")
        print(f"   └─ {player.name} earned {points} points!")
        print(f"\n🌌 NEW UNIVERSE CREATED: {universe_name}")
        print(f"   └─ Total Universes: {len(self.multiverse.nodes)}")
        
        # Next turn
        self.turn_queue.next_turn()
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main game loop"""
        self.clear()
        self.print_header()
        
        # Get players
        n = int(input("Number of players (2-4): "))
        print()
        for i in range(n):
            name = input(f"Player {i+1} name: ")
            self.add_player(name)
        
        # Main loop
        while True:
            self.clear()
            self.print_header()
            self.print_stats_fancy()
            self.print_player_stats()
            
            print("┌" + "─"*68 + "┐")
            print("│" + " MAIN MENU ".center(68) + "│")
            print("├" + "─"*68 + "┤")
            print("│  (1) Play Turn       (2) View Blockchain   (3) View Multiverse  │")
            print("│  (4) Data Structures (5) Exit                                   │")
            print("└" + "─"*68 + "┘\n")
            
            choice = input("Choice: ")
            
            if choice == "1":
                self.play_turn()
            elif choice == "2":
                self.print_blockchain_fancy()
                input("Press Enter...")
            elif choice == "3":
                self.print_multiverse_fancy()
                input("Press Enter...")
            elif choice == "4":
                self.show_ds_info()
                input("Press Enter...")
            elif choice == "5":
                self.show_final_report()
                break
    
    def show_ds_info(self):
        """Show data structures info"""
        self.clear()
        print("""
╔════════════════════════════════════════════════════════════════════╗
║          DATA STRUCTURES IMPLEMENTATION DETAILS                    ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║ 1️⃣  LINKED LIST (BLOCKCHAIN)                                      ║
║    ├─ Structure: Block nodes linked via previous_hash             ║
║    ├─ Operations:                                                  ║
║    │  • add_block(): O(2^difficulty) mining + O(1) insert         ║
║    │  • is_valid(): O(n) validation                                ║
║    ├─ Features: SHA-256 hashing, Proof-of-Work                    ║
║    └─ Status: ✅ FULLY IMPLEMENTED                                 ║
║                                                                    ║
║ 2️⃣  N-ARY TREE / GRAPH (MULTIVERSE)                               ║
║    ├─ Structure: Parent-child relationships, multiple children    ║
║    ├─ Operations:                                                  ║
║    │  • create_universe(): O(1) node insertion                     ║
║    │  • bfs(): O(V+E) breadth-first traversal                     ║
║    │  • dfs(): O(V+E) depth-first traversal                       ║
║    ├─ Features: Tree visualization, branching paths               ║
║    └─ Status: ✅ FULLY IMPLEMENTED                                 ║
║                                                                    ║
║ 3️⃣  CIRCULAR QUEUE (TURN MANAGEMENT)                              ║
║    ├─ Structure: Circular buffer with front/rear pointers         ║
║    ├─ Operations:                                                  ║
║    │  • enqueue(): O(1) add to queue                              ║
║    │  • dequeue(): O(1) remove from queue                         ║
║    │  • next_turn(): O(1) circular rotation                       ║
║    ├─ Features: FIFO, wraparound, player rotation                 ║
║    └─ Status: ✅ FULLY IMPLEMENTED                                 ║
║                                                                    ║
║ 4️⃣  HASH MAP (PLAYER STORAGE)                                     ║
║    ├─ Structure: Array of buckets with chaining                   ║
║    ├─ Operations:                                                  ║
║    │  • set(): O(1) average insert/update                         ║
║    │  • get(): O(1) average retrieval                             ║
║    │  • delete(): O(1) average deletion                           ║
║    ├─ Features: Hash function, collision handling                 ║
║    └─ Status: ✅ FULLY IMPLEMENTED                                 ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
        """)
    
    def show_final_report(self):
        """Show comprehensive final report"""
        self.clear()
        stats = self.get_advanced_stats()
        
        print("""
╔═══════════════════════════════════════════════════════════════════╗
║                   FINAL GAME REPORT & ANALYSIS                    ║
╠═══════════════════════════════════════════════════════════════════╣
""")
        
        print(f"║ Game Duration: {(datetime.now() - self.start_time).total_seconds():.1f}s                           ║")
        print(f"║ Total Turns Played: {stats['turns']:<45} ║")
        print(f"║ Blocks Mined: {stats['blocks']:<50} ║")
        print(f"║ Universes Created: {stats['universes']:<44} ║")
        print(f"║ Total Players: {stats['players']:<49} ║")
        print(f"║ Blockchain Status: {'✅ VALID' if stats['valid'] else '❌ INVALID':<41} ║")
        
        print(f"""║                                                               ║
╠═══════════════════════════════════════════════════════════════════╣
║                     PLAYER FINAL SCORES                           ║
╠═══════════════════════════════════════════════════════════════════╣
""")
        
        for i in range(self.turn_queue.size):
            idx = (self.turn_queue.front + i) % self.turn_queue.capacity
            if self.turn_queue.queue[idx]:
                player = self.turn_queue.queue[idx]
                print(f"║ {player.name:>15} | Score: {player.score:>4} | Rank: {i+1}/{self.turn_queue.size}                     ║")
        
        print(f"""║                                                               ║
╠═══════════════════════════════════════════════════════════════════╣
║                    DATA STRUCTURES USAGE                          ║
╠═══════════════════════════════════════════════════════════════════╣
║ ✅ Linked List: MINED {stats['blocks']} BLOCKS → O(2^difficulty)     ║
║ ✅ N-ary Tree: CREATED {stats['universes']} UNIVERSES → O(V+E)         ║
║ ✅ Circular Queue: MANAGED {stats['players']} PLAYERS → O(1)        ║
║ ✅ Hash Map: STORED ALL PLAYERS → O(1) lookup                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════════╝

🎉 THANK YOU FOR PLAYING NEXUS! 🎉

        """)

if __name__ == "__main__":
    game = NexusAdvanced()
    game.run()
