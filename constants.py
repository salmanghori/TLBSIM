import math

# general settings
MACHINE_TYPE = 32

# general constants
MASK64 = 0xffffffffffffffff
MASK32 = 0xffffffff
PAGE_SIZE4K = 4 * 1024

# simulated machine 
PAGE_SIZE = PAGE_SIZE4K
MASK_MACHINE = MASK32

MASK_TAG = (MASK32 << int(math.log(PAGE_SIZE, 2))) & MASK_MACHINE
MASK_OFFSET = (~(MASK32 << int(math.log(PAGE_SIZE, 2)))) & MASK_MACHINE


def get_offset(vaddr):
  return (MASK_OFFSET & vaddr)

def get_tag(vaddr):
  return (MASK_TAG & vaddr) >> int(math.log(PAGE_SIZE, 2))

# def get_index(vaddr):
#   return get_tag(vaddr) & (~(0xff))

# ----------------------------------------------------------------------
# def get_offset(vaddr):
#   return vaddr % PAGE_SIZE

# def get_tag(vaddr):
#   return int(vaddr / PAGE_SIZE)

# def get_index(vaddr):
#   return gettag(vaddr) % 256
