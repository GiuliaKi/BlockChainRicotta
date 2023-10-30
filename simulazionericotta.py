import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Inizio della filiera della produzione della ricotta di pecora")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

# Creazione di una istanza della blockchain
blockchain = Blockchain()

# Allevamento
blockchain.add_block("Pecore nutrite e alloggiate")

# Produzione di latte
blockchain.add_block("Mungitura delle pecore")

# Lavorazione del latte in ricotta
blockchain.add_block("Produzione di ricotta")

# Vendita in supermercato
blockchain.add_block("Ricotta confezionata e venduta in supermercato")

# Visualizza i dettagli dei blocchi
for block in blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("\n")

# Verifica l'integrità della blockchain
def verify_blockchain(blockchain):
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i - 1]

        if current_block.hash != current_block.calculate_hash():
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

    return True

print("La Blockchain è valida:", verify_blockchain(blockchain))
