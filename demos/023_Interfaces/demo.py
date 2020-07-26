bob = Villain("bob", "name without caps")
bob.laugh()
# AssertionError: Haven't defined laugh() yet

bob(args)


dv = DarthVader("Darth Vader", "Big scary force powers")
dv.laugh()
dv.warble("use the net force")
# warble
# use the net force
# hooo paahhhh
dv.forcePush()
#
z1 = Zombie("zomb1", "slow movement, lack of brain")
z1.laugh()
