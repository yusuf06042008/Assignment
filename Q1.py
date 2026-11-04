
# Program to calculate Effective Address
# for different Addressing Modes

address = 200
R1 = 40

memory = {
    200: 500,
    240: 900
}

# (a) Immediate Addressing
immediate_operand = 25
print("a) Immediate Addressing")
print("Operand Value =", immediate_operand)

# (b) Direct Addressing
direct_EA = address
print("\nb) Direct Addressing")
print("Effective Address =", direct_EA)
print("Operand Value =", memory[direct_EA])

# (c) Indirect Addressing
indirect_EA = memory[address]
print("\nc) Indirect Addressing")
print("Effective Address =", indirect_EA)

if indirect_EA in memory:
    print("Operand Value =", memory[indirect_EA])
else:
    print("Operand Value = Not Given")

# (d) Indexed Addressing
indexed_EA = address + R1
print("\nd) Indexed Addressing")
print("Effective Address =", indexed_EA)
print("Operand Value =", memory[indexed_EA])






