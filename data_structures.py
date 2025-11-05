"""
NEXUS: Multiverse Truth or Dare - All Data Structures
Student: [Your Name]
Roll No: [Your Roll]
Date: November 2025
"""

import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional
import random

# ============================================
# DATA STRUCTURE 1: LINKED LIST (BLOCKCHAIN)
# ============================================

class Block:
    """Blockchain Node - Linked List"""
    
    def __init__(self, index: int, data: Dict, previous_hash: str = "0"):
        self.index = index
        self.timestamp = datetime.now().timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """SHA-256 hashing"""
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int):
        """Proof of Work - O(2^difficulty)"""
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"⛏️  Block #{self.index} mined!")

class Blockchain:
    """Linked List Implementation"""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.difficulty = 2
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_data = {"player": "SYSTEM", "type": "GENESIS", "challenge": "Game Start"}
        self.chain.append(Block(0, genesis_data, "0"))
    
    def add_block(self, data: Dict) -> Block:
        """Add block - O(n) with mining"""
        new_block = Block(len(self.chain), data, self.chain[-1].hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block
    
    def is_valid(self) -> bool:
        """Validate chain - O(n)"""
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

# ============================================
# DATA STRUCTURE 2: N-ARY TREE (MULTIVERSE)
# ============================================

class UniverseNode:
    """Tree Node for Multiverse"""
    
    def __init__(self, uid: str, name: str):
        self.id = uid
        self.name = name
        self.children: List['UniverseNode'] = []
        self.parent: Optional['UniverseNode'] = None

class MultiverseGraph:
    """N-ary Tree Implementation"""
    
    def __init__(self):
        self.root = UniverseNode("PRIME", "Prime Reality")
        self.nodes = {"PRIME": self.root}
        self.count = 0
    
    def create_universe(self, parent_id: str, name: str) -> UniverseNode:
        """Create branch - O(1)"""
        parent = self.nodes.get(parent_id)
        if not parent:
            return None
        
        self.count += 1
        uid = f"UNI-{self.count}"
        node = UniverseNode(uid, name)
        node.parent = parent
        parent.children.append(node)
        self.nodes[uid] = node
        return node
    
    def bfs(self) -> List[UniverseNode]:
        """Breadth-First Search - O(V+E)"""
        visited = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            visited.append(node)
            queue.extend(node.children)
        return visited
    
    def dfs(self) -> List[UniverseNode]:
        """Depth-First Search - O(V+E)"""
        visited = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            visited.append(node)
            stack.extend(reversed(node.children))
        return visited

# ============================================
# DATA STRUCTURE 3: CIRCULAR QUEUE
# ============================================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

class TurnQueue:
    """Circular Queue - FIFO"""
    
    def __init__(self, capacity: int = 10):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity
    
    def enqueue(self, player: Player) -> bool:
        """Add to queue - O(1)"""
        if self.size == self.capacity:
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = player
        self.size += 1
        return True
    
    def dequeue(self) -> Optional[Player]:
        """Remove from queue - O(1)"""
        if self.size == 0:
            return None
        player = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return player
    
    def next_turn(self) -> Optional[Player]:
        """Circular rotation - O(1)"""
        if self.size == 0:
            return None
        player = self.dequeue()
        self.enqueue(player)
        return self.queue[self.front]
    
    def peek(self) -> Optional[Player]:
        """View current - O(1)"""
        return self.queue[self.front] if self.size > 0 else None

# ============================================
# DATA STRUCTURE 4: HASH MAP
# ============================================

class HashMap:
    """Hash Table with Chaining"""
    
    def __init__(self, size: int = 16):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key: str) -> int:
        """Hash function"""
        return hash(key) % self.size
    
    def set(self, key: str, value) -> None:
        """Insert - O(1) average"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
        self.count += 1
    
    def get(self, key: str):
        """Retrieve - O(1) average"""
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key: str) -> bool:
        """Remove - O(1) average"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].pop(i)
                self.count -= 1
                return True
        return False

# ============================================
# CHALLENGE SYSTEM
# ============================================

CHALLENGES = {
    "TRUTH": [
        "What is your most embarrassing moment?",
        "Who do you have a crush on?",
        "What's your biggest secret?",
        "Have you ever cheated?",
    ],
    "DARE": [
        "Do 10 push-ups right now",
        "Dance for 30 seconds",
        "Call someone and sing",
        "Post something embarrassing",
    ]
}

def get_random_challenge(ctype: str) -> str:
    return random.choice(CHALLENGES[ctype])
