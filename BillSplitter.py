def main():
    # Get household member names
    print("=== Grocery Bill Splitter ===\n")

    num_members = int(input("Enter the number of members in your household: "))
    
    members = []
    for i in range(num_members):
        name = input(f"Enter name of person {i+1}: ").strip()
        members.append(name)
    
    print(f"\nHousehold members: {', '.join(members)}")
    
    # Get who paid the bill
    print("\nWho paid the entire bill?")
    for i, name in enumerate(members, 1):
        print(f"{i}. {name}")
    payer_idx = int(input("Enter number: ")) - 1
    payer = members[payer_idx]
    
    # Initialize tracking
    items = []
    person_totals = {name: 0.0 for name in members}
    
    # Enter items
    print("\n=== Enter Items ===")
    print("(Press Enter with empty item name when done)\n")
    
    while True:
        item_name = input("Item name: ").strip()
        if not item_name:
            break
        
        price = float(input("Price: $"))
        
        print("Who wants this item? (enter numbers separated by spaces)")
        for i, name in enumerate(members, 1):
            print(f"{i}. {name}")
        
        buyers_input = input("Numbers: ").strip()
        buyer_indices = [int(x) - 1 for x in buyers_input.split()]
        buyers = [members[i] for i in buyer_indices]
        
        # Calculate split amount
        split_amount = price / len(buyers)
        
        # Add to each buyer's total
        for buyer in buyers:
            person_totals[buyer] += split_amount
        
        items.append({
            'name': item_name,
            'price': price,
            'buyers': buyers,
            'split': split_amount
        })
        
        print(f"Added: {item_name} - ${price:.2f} split among {len(buyers)} people (${split_amount:.2f} each)\n")
    
    # Display results
    print("\n" + "="*50)
    print("BILL SUMMARY")
    print("="*50)
    
    total_bill = sum(item['price'] for item in items)
    print(f"\nTotal Bill: ${total_bill:.2f}")
    print(f"Paid by: {payer}\n")
    
    print("Item Breakdown:")
    print("-" * 50)
    for item in items:
        buyers_str = ", ".join(item['buyers'])
        print(f"{item['name']}: ${item['price']:.2f}")
        print(f"  Split among: {buyers_str} (${item['split']:.2f} each)")
    
    print("\n" + "="*50)
    print("WHO OWES WHAT")
    print("="*50 + "\n")
    
    for name in members:
        amount = person_totals[name]
        if name == payer:
            print(f"{name}: Paid ${total_bill:.2f}, owes ${amount:.2f} → Net: ${amount - total_bill:.2f}")
        else:
            if amount > 0:
                print(f"{name} owes {payer}: ${amount:.2f}")
            else:
                print(f"{name}: $0.00 (didn't want any items)")

if __name__ == "__main__":
    main()
