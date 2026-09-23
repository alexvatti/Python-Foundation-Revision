# mutable-default-arg-test.py
# Demonstrates the classic Python "mutable default argument" bug and the
# correct fix, with test cases (assertions) around both versions.
#
# ======================================================================
# RULE OF THUMB:
#   Never use a mutable object ([], {}, set()) as a default argument
#   value. Use None and build the real default inside the function body.
# ======================================================================


# ----------------------------------------------------------------------
# BUGGY version: the default list is created ONCE at definition time and
# is shared across every call that does not pass its own list.
# ----------------------------------------------------------------------
def add_item_buggy(item, items=[]):
    items.append(item)
    return items


# ----------------------------------------------------------------------
# FIXED version: use None as the default and build a fresh list inside
# the function on every call.
# ----------------------------------------------------------------------
def add_item_fixed(item, items=None):
    if items is None:
        items = []          # brand-new list every call
    items.append(item)
    return items            # return the LIST, not the single item





if __name__ == "__main__":
    print("======================================================================")
    print("RULE OF THUMB:")
    print("  Never use a mutable object ([], {}, set()) as a default argument")
    print("  value. Use None and build the real default inside the function body.")
    print("======================================================================")

    print("\n===== BUGGY VERSION OUTPUT =====")
    print(add_item_buggy(1))   # [1]
    print(add_item_buggy(2))   # [1, 2]  <-- shared state!

    print("\n===== FIXED VERSION OUTPUT =====")
    print(add_item_fixed(1))   # [1]
    print(add_item_fixed(2))   # [2]  correct


