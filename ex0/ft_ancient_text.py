if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        fd = open("../data-generator-tools/ancient_fragment.txt", 'r')
        print("Connection established...\n")
        content = fd.read()
        fd.close()
        print(f"RECOVERED DATA:\n{content}\n")
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
