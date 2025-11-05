
<div align="center">

<!-- Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=NEXUS&fontSize=80&fontAlignY=35&animation=twinkling&fontColor=00ffff" />

# 🌌 NEXUS: MULTIVERSE TRUTH OR DARE 🌌

### *Where Every Choice Shatters Reality and Creates New Universes*

[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18.2-61dafb?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.2-007acc?style=for-the-badge&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![Blockchain](https://img.shields.io/badge/Blockchain-Enabled-00ff00?style=for-the-badge&logo=bitcoin&logoColor=white)](https://blockchain.info)

**A Groundbreaking Data Structures Project That Actually Makes Sense**

[🚀 Quick Start](#-installation) • [🎮 Play Demo](#-how-to-play) • [📖 Read Docs](#-documentation) • [🎥 Watch Video](#-demo-video) • [⭐ Star Project](#)

<img src="https://img.shields.io/github/stars/Aryan-lomte05/Nexus-Truth-or-Dare-DSA?style=social" />
<img src="https://img.shields.io/github/forks/Aryan-lomte05/Nexus-Truth-or-Dare-DSA?style=social" />
<img src="https://img.shields.io/badge/Made%20with-Love%20%26%20Code-ff69b4?style=flat-square" />

---

### **🏆 The Only Truth or Dare Game With:**
✅ Real Blockchain Technology (SHA-256 + Proof-of-Work)  
✅ Parallel Universe Branching (Quantum Computing Inspired)  
✅ Cryptographically Secure Game History  
✅ Professional-Grade Data Structures  

</div>

---

## 🎯 **What Is NEXUS?**

Imagine if **Bitcoin** met **Rick and Morty's Multiverse** and they decided to play **Truth or Dare**.

That's NEXUS.

**NEXUS** is not your average college project. It's a fully functional game that teaches you:
- How blockchains ACTUALLY work (not just theory)
- Why trees are everywhere in computer science
- How your favorite games manage millions of players
- Why hash tables make Google search instant

Built with **Python** (backend logic) and **React/TypeScript** (killer UI), this project demonstrates **4 fundamental data structures** that power the modern world.

---

## ⚡ **The Problem We're Solving**

Most data structures projects are boring:
- ❌ "Here's a linked list that prints numbers"
- ❌ "Look, my tree can store names"
- ❌ "Check out this queue... doing nothing"

**NEXUS is different:**
- ✅ Blockchain that actually secures data with cryptography
- ✅ Multiverse that tracks alternate realities
- ✅ Queue that manages real gameplay turns
- ✅ HashMap that powers lightning-fast lookups

---

## 🔥 **Key Features**

<table>
<tr>
<td width="50%">

### 🔐 **Blockchain Technology**
- **SHA-256 Cryptographic Hashing**
- **Proof-of-Work Mining** (difficulty adjustable)
- **Immutable History** (tamper-proof)
- **Chain Validation** (instant integrity checks)
- Real Bitcoin-style consensus mechanism

*Every game action is permanently recorded in an unchangeable chain*

</td>
<td width="50%">

### 🌌 **Multiverse System**
- **Parallel Universe Branching**
- **BFS/DFS Tree Traversal**
- **Decision Tree Visualization**
- **Alternate Timeline Tracking**
- Quantum-inspired reality splitting

*Each choice creates a new branch in the multiverse tree*

</td>
</tr>
<tr>
<td width="50%">

### 🎮 **Gameplay Features**
- **20+ Dynamic Challenges** (Truth & Dare)
- **Difficulty Scaling** (Easy → Insane)
- **Real-time Statistics**
- **Multiple Interfaces** (CLI, GUI, Web)
- Score tracking and leaderboards

*Actual fun gameplay, not just a demo*

</td>
<td width="50%">

### ⚡ **Performance Optimized**
- **O(1) Queue Operations**
- **O(1) HashMap Lookups** (average)
- **O(V+E) Graph Traversal**
- **O(2^d) Secure Mining**
- Production-ready algorithms

*Every operation is analyzed and optimized*

</td>
</tr>
</table>

---

## 🏗️ **Architecture Overview**
```sh
┌─────────────────────────────────────────────────────────────┐
│ NEXUS ARCHITECTURE │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────────┐ ┌──────────────────┐ │
│ │ BLOCKCHAIN │◄───────►│ MULTIVERSE │ │
│ │ (Linked List) │ │ (N-ary Tree) │ │
│ └────────┬─────────┘ └────────┬─────────┘ │
│ │ │ │
│ │ ┌───────────────────┐ │ │
│ └───► GAME ENGINE ◄───┘ │
│ └────────┬──────────┘ │
│ │ │
│ ┌────────────┴────────────┐ │
│ │ │ │
│ ┌────────▼─────────┐ ┌─────────▼────────┐ │
│ │ TURN QUEUE │ │ HASH MAP │ │
│ │ (Circular Queue) │ │ (Player Storage) │ │
│ └──────────────────┘ └──────────────────┘ │
│ │
├─────────────────────────────────────────────────────────────┤
│ USER INTERFACES │
├─────────────────────────────────────────────────────────────┤
│ [CLI Console] [Advanced CLI] [GUI Tkinter] [React Web] │
└─────────────────────────────────────────────────────────────┘

```

---

## 📊 **Data Structures Deep Dive**

### 1️⃣ **BLOCKCHAIN (Linked List)** 🔗

> *"The same technology that secures $800 billion in cryptocurrency"*

<details>
<summary><b>Click to expand implementation details</b></summary>

class Block:
"""
Blockchain Node - Singly Linked List with Cryptographic Linking

text
Each block contains:
- Index: Position in chain
- Timestamp: When it was created
- Data: Game action (player, challenge, response)
- Previous Hash: Link to previous block (cryptographic)
- Hash: This block's unique fingerprint
- Nonce: Proof-of-Work solution
"""

def calculate_hash(self) -> str:
    """SHA-256 hashing - same as Bitcoin"""
    block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}{self.nonce}"
    return hashlib.sha256(block_string.encode()).hexdigest()

def mine_block(self, difficulty: int):
    """
    Proof-of-Work Mining
    Finds a nonce that makes hash start with 'difficulty' zeros
    
    Time Complexity: O(2^difficulty)
    Why? Need to try random numbers until we find one that works
    """
    target = "0" * difficulty
    while self.hash[:difficulty] != target:
        self.nonce += 1
        self.hash = self.calculate_hash()
text

**Operations & Complexity:**
| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `add_block()` | O(2^d) | Proof-of-Work makes it hard to fake |
| `is_valid()` | O(n) | Must check each block's connection |
| `get_block()` | O(n) | Linear search through chain |
| `mine_block()` | O(2^d) | Exponential - security requirement |

**Real-World Applications:**
- 💰 Bitcoin, Ethereum (cryptocurrency)
- 📦 Supply chain tracking
- 🏥 Medical records
- 🗳️ Voting systems

</details>

---

### 2️⃣ **MULTIVERSE GRAPH (N-ary Tree)** 🌳

> *"Every decision branches into parallel universes"*

<details>
<summary><b>Click to expand implementation details</b></summary>

class UniverseNode:
"""
N-ary Tree Node - Each node can have unlimited children

text
Represents one universe in the multiverse:
- Prime Reality (Root)
  ├─ Aryan's TRUTH Universe (Child 1)
  ├─ Lomte's TRUTH Universe (Child 2)
  └─ Ary's DARE Universe (Child 3)
"""

def __init__(self, uid: str, name: str):
    self.id = uid
    self.name = name
    self.children = []  # Can have many children!
    self.parent = None
class MultiverseGraph:
"""Manages entire multiverse tree"""

text
def bfs(self) -> List[UniverseNode]:
    """
    Breadth-First Search
    Explores level by level (like ripples in water)
    
    Time Complexity: O(V + E)
    V = number of universes, E = connections between them
    """
    visited = []
    queue = [self.root]
    
    while queue:
        node = queue.pop(0)
        visited.append(node)
        queue.extend(node.children)
    
    return visited
text

**Operations & Complexity:**
| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `create_universe()` | O(1) | Just add new node |
| `bfs()` | O(V + E) | Visit every universe and connection |
| `dfs()` | O(V + E) | Depth-first exploration |
| `get_depth()` | O(h) | h = height of tree |

**Real-World Applications:**
- 📁 File systems (folders/subfolders)
- 🌐 Website DOM (HTML structure)
- 🎮 Game decision trees
- 🤖 AI decision making

</details>

---

### 3️⃣ **TURN QUEUE (Circular Queue)** 🔄

> *"Fair turn system that never ends"*

<details>
<summary><b>Click to expand implementation details</b></summary>

class TurnQueue:
"""
Circular Queue - Like musical chairs that never stops

text
[Lomte] → [Ary] → [Aryan] → back to [Lomte]

Uses modular arithmetic for circular wrapping:
rear = (rear + 1) % capacity
"""

def next_turn(self) -> Player:
    """
    Circular Rotation - O(1) constant time!
    
    1. Remove player from front
    2. Add same player to back
    3. Next player is now at front
    
    No matter how many players, always O(1)!
    """
    player = self.dequeue()
    self.enqueue(player)
    return self.peek()
text

**Operations & Complexity:**
| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `enqueue()` | O(1) | Add to rear - instant |
| `dequeue()` | O(1) | Remove from front - instant |
| `next_turn()` | O(1) | Circular rotation - instant |
| `peek()` | O(1) | Look at front - instant |

**Real-World Applications:**
- 🖨️ Printer job scheduling
- 🍕 Restaurant order queues
- 🎮 Multiplayer game turns
- ⚙️ CPU task scheduling

</details>

---

### 4️⃣ **HASH MAP (Hash Table)** 📚

> *"Find any player instantly from millions"*

<details>
<summary><b>Click to expand implementation details</b></summary>

class HashMap:
"""
Hash Table with Chaining

text
Like a filing cabinet with a magic formula:
- Formula tells you exact drawer to look in
- O(1) average time - INSTANT!

Drawers (Buckets):
: []
: []​
: [(Aryan, score=10)] ← Hash function says "Aryan goes in drawer 2"​
: []​
: [(Lomte, score=25), (Lom, score=5)] ← Collision handled with chain​
...
"""

text
def _hash(self, key: str) -> int:
    """
    Hash Function - The magic formula
    Takes player name → Returns drawer number
    
    hash("Aryan") = some big number % 16 = 2
    So Aryan goes in drawer 2!
    """
    return hash(key) % self.size

def get(self, key: str):
    """
    Find player - O(1) average time
    1. Use hash function to find drawer
    2. Open that drawer
    3. FOUND! (or search chain if collision)
    """
    index = self._hash(key)
    for k, v in self.buckets[index]:
        if k == key:
            return v
    return None
text

**Operations & Complexity:**
| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `set()` | O(1) avg | Hash to drawer, insert |
| `get()` | O(1) avg | Hash to drawer, retrieve |
| `delete()` | O(1) avg | Hash to drawer, remove |
| `resize()` | O(n) | When too full, rebuild |

**Real-World Applications:**
- 🔍 Google search indexing
- 💾 Database indexing
- 🗂️ Python dictionaries
- 🌐 DNS lookups

</details>

---

## 🚀 **Installation**

### **Option 1: Python CLI/GUI (Recommended for Learning)**

Clone repository
git clone https://github.com/Aryan-lomte05/Nexus-Truth-or-Dare-DSA.git
cd Nexus-Truth-or-Dare-DSA

No dependencies needed! Pure Python 3.11+
Run basic console version
python python-implementation/nexus_cli.py

Run advanced console version (beautiful output)
python python-implementation/nexus_advanced.py

Run GUI version (Tkinter - comes with Python)
python python-implementation/nexus_gui_premium.py

---

## 📈 **Performance Benchmarks**

### **Complexity Analysis Summary**
```sh
┌─────────────────┬─────────────────┬──────────────────┬────────────────┐
│ Data Structure │ Operation │ Time Complexity │ Space Complexity│
├─────────────────┼─────────────────┼──────────────────┼────────────────┤
│ Linked List │ Add Block │ O(2^difficulty) │ O(1) │
│ (Blockchain) │ Validate Chain │ O(n) │ O(1) │
│ │ Search Block │ O(n) │ O(1) │
├─────────────────┼─────────────────┼──────────────────┼────────────────┤
│ N-ary Tree │ Insert Node │ O(1) │ O(1) │
│ (Multiverse) │ BFS Traversal │ O(V + E) │ O(V) │
│ │ DFS Traversal │ O(V + E) │ O(h) │
├─────────────────┼─────────────────┼──────────────────┼────────────────┤
│ Circular Queue │ Enqueue │ O(1) │ O(1) │
│ (Turns) │ Dequeue │ O(1) │ O(1) │
│ │ Next Turn │ O(1) │ O(1) │
├─────────────────┼─────────────────┼──────────────────┼────────────────┤
│ Hash Map │ Insert/Get │ O(1) average │ O(n) │
│ (Players) │ Delete │ O(1) average │ O(n) │
│ │ Resize │ O(n) │ O(n) │
└─────────────────┴─────────────────┴──────────────────┴────────────────┘

```

### **Why These Complexities Matter:**

🔐 **Blockchain Mining O(2^d):**  
Making it hard to add blocks = SECURITY. This is intentional!  
Bitcoin uses the same principle - makes attacks expensive.

🌳 **Tree Traversal O(V+E):**  
Visit every universe exactly once = EFFICIENCY  
Can't do better than this for exploring all nodes.

⚡ **Queue O(1):**  
Constant time = FAIRNESS  
No matter how many players, everyone waits the same.

📚 **HashMap O(1) avg:**  
Instant lookups = SPEED  
Finding one player in a million takes same time as finding in ten.

---

## 🎓 **Educational Value**

### **What You'll Learn:**

<table>
<tr>
<td width="50%">

#### 🧠 **Computer Science Concepts**
- Cryptographic hashing (SHA-256)
- Proof-of-Work consensus
- Graph theory and traversal
- Queue data structures
- Hash table collision resolution
- Big-O complexity analysis
- Modular arithmetic

</td>
<td width="50%">

#### 🛠️ **Software Engineering**
- Clean code principles
- Object-oriented design
- Algorithm optimization
- Test-driven development
- Version control (Git)
- Documentation
- Project architecture

</td>
</tr>
</table>

### **Real-World Skills:**

✅ **Blockchain Development** - Understand crypto fundamentals  
✅ **Algorithm Design** - Optimize for performance  
✅ **System Architecture** - Build scalable systems  
✅ **Problem Solving** - Think like an engineer  

---

## 🎥 **Demo Video**

<div align="center">

[![Watch Demo](https://img.shields.io/badge/▶️-Watch%20Full%20Demo-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1kJ3l_yFuvN8v-fQA0kO1O_YQHIpItECT/view?usp=drive_link)

**5-minute walkthrough covering:**
- Live gameplay demonstration
- Blockchain mining in action
- Multiverse branching visualization
- Code architecture overview
- Complexity analysis

</div>

---
## 🤝 **Contributing**

Want to make NEXUS even more legendary? Contributions welcome!

Fork the repository
Create feature branch
git checkout -b feature/AmazingFeature

Commit changes
git commit -m 'Add AmazingFeature'

Push to branch
git push origin feature/AmazingFeature

Open Pull Request


---
## 📜 **License**

MIT License - See [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Bitcoin** - For showing us how blockchains work
- **Ayesha Maam** - For teaching data structures
- **Coffee** - For making this possible at 3 AM

---

## 📞 **Contact**

<div align="center">

**Aryan Lomte**

[![GitHub](https://img.shields.io/badge/GitHub-Aryan--lomte05-181717?style=for-the-badge&logo=github)](https://github.com/Aryan-lomte05)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077b5?style=for-the-badge&logo=linkedin)](www.linkedin.com/in/aryan-lomte-99ab68310)
[![Email](https://img.shields.io/badge/Email-aryanlomte05@gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aryanlomte05@gmail.com)

**Course:** BTech Computer Science & Business Systems  
**Institution:** KJ Somaiya School of Engineering  
**Year:** 2025

</div>

---

## 💡 **Fun Facts**

- 🏆 This project uses the **SAME hashing algorithm as Bitcoin** (SHA-256)
- 🌌 The multiverse can theoretically track **infinite parallel realities**
- ⚡ With O(1) operations, the game **scales to unlimited players**
- 🔒 The blockchain is **cryptographically secure** - same as real crypto
- 🎮 It's **actually fun to play** - not just a boring demo!

---

## 🚀 **Future Roadmap**

- [ ] AI-powered challenge generation (GPT integration)
- [ ] Real cryptocurrency rewards (Ethereum integration)
- [ ] Mobile app (React Native)
- [ ] Multiplayer online mode (WebSockets)
- [ ] NFT universe minting (Blockchain art)
- [ ] VR multiverse exploration
- [ ] Global leaderboard

---

<div align="center">

## ⭐ **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=Aryan-lomte05/Nexus-Truth-or-Dare-DSA&type=Date)](https://star-history.com/#Aryan-lomte05/Nexus-Truth-or-Dare-DSA&Date)

---

### **If this project helped you understand data structures, give it a ⭐**

### **If it blew your mind, give it a ⭐⭐⭐⭐⭐**

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" />

**Made with 💜 by Aryan Lomte | 2025**

*"In the multiverse, every possibility exists. Make your choice count."*

</div>