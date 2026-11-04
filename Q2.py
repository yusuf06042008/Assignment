
# Virtual Address to Physical Address Translation

PAGE_SIZE = 1024

# Page Table: Virtual Page -> Frame Number
page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7
}

# Given virtual addresses
addresses = [500, 1500, 2500, 3500]

print("Virtual Address Translation")
print("--------------------------------")

for address in addresses:

    # Calculate page number and offset
    page_number = address // PAGE_SIZE
    offset = address % PAGE_SIZE

    print("\nVirtual Address:", address)
    print("Page Number:", page_number)
    print("Offset:", offset)

    # Check page table
    if page_number in page_table and page_table[page_number] is not None:

        frame_number = page_table[page_number]

        # Calculate physical address
        physical_address = (frame_number * PAGE_SIZE) + offset

        print("Frame Number:", frame_number)
        print("Physical Address:", physical_address)

    else:
        print("Page Fault!")
