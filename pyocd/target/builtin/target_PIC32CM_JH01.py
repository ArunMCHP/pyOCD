# pyOCD debugger
# Copyright (c) 2025 Microchip Technology Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap, MemoryRegion)

'''
# No issues with harmony
MAIN_FLASH_ALGO = {
    'load_address': 0x20000000,

    'instructions': [
        0xe7fdbe00,
        0x074a492d, 0x4a2e6011, 0x6051492c, 0x4449492d, 0x20006008,
        0x20004770, 0x210f4770, 0x400103c9, 0x200f0842, 0x40020380,
        0x4825b510, 0x4a2661c2, 0x69428002, 0xd0fc07d2, 0x22014c23,
        0x03d23c3f, 0xe00c188b, 0x61c2084a, 0x69428004, 0xd0fc07d2,
        0x07926942, 0x2001d501, 0x31ffbd10, 0x42993101, 0x2000d3f0,
        0xb5f0bd10, 0x08891cc9, 0x00894b16, 0x1cdb4d13, 0x696b802b,
        0xd0fc07db, 0x3e3d4e12, 0xd0162900, 0x29404603, 0x2440d901,
        0x460ce005, 0xca80e003, 0xc3801f09, 0x2c001f24, 0x802ed1f9,
        0x696b3040, 0xd0fc07db, 0x079b696b, 0x2001d5e8, 0x2000bdf0,
        0x0000bdf0, 0x00010022, 0x0004009e, 0x41004000, 0x00000004,
        0x0000a541, 0x00000000, 0x00000000
    ],

    # ENTRY POINTS: absolute addresses computed from the symbol offsets
    'pc_init'         : 0x20000000 + 0x01,   # 0x20000001
    'pc_unInit'       : 0x20000000 + 0x17,   # 0x20000017
    'pc_program_page' : 0x20000000 + 0x67,   # 0x20000067
    'pc_erase_sector' : 0x20000000 + 0x1b,   # 0x2000001b
    'pc_eraseAll'     : 0xFFFFFFFF,

    'static_base'  : 0x20000000 + 0x4 + 0xcc,   # unchanged (0x200000d0)
    'begin_data'   : 0x20002000,                # page buffers start well above Zephyr usage
    'page_buffers' : [
        0x20002000,   # buffer0
        0x20002400,   # buffer1
    ],
    # buffers occupy up to 0x200027FF -> place stack bottom just above
    'end_stack'    : 0x20002800,
    'begin_stack'  : 0x20010000,                # top of SRAM (64 KiB device)

    'page_size'            : 0x400,
    'min_program_length'   : 0x400,

    'analyzer_supported' : False,
    'analyzer_address'   : 0x00000000,

    # internal layout copied from your ELF map
    'ro_start' : 0x4,
    'ro_size'  : 0xcc,   # matches .text RO size shown in armlink
    'rw_start' : 0xd0,
    'rw_size'  : 0x8,
    'zi_start' : 0xd8,
    'zi_size'  : 0x0,

    'flash_start' : 0x00000000,
    'flash_size'  : 0x00080000,
    'sector_sizes': ((0x0, 0x8000),),
}

DATA_FLASH_ALGO = {
    'load_address' : 0x20000000,

    'instructions': [
        0xe7fdbe00,
        0x074a491c, 0x4a1d6011, 0x6051491b, 0x4449491c, 0x20006008,
        0x20004770, 0x08414770, 0x61c14817, 0x80014918, 0x07c96941,
        0x6940d0fc, 0xd5010780, 0x47702001, 0x47702000, 0x4c12b510,
        0x342a4b0f, 0x695c801c, 0xd0fc07e4, 0x08891cc9, 0xe0020089,
        0x1f09ca10, 0x2900c010, 0x480ad1fa, 0x80181c80, 0x07c06958,
        0x6958d0fc, 0xd5010780, 0xbd102001, 0xbd102000, 0x00010022,
        0x0004009e, 0x41004000, 0x00000004, 0x0000a51a, 0x00000000,
        0x00000000
    ],

    # ENTRY POINTS: use the same offsets (init/uninit/erase/program) from the data blob's symbol table
    # If your data-flash FLM compiled had different offsets, replace these with the data-blob symbol offsets.
    'pc_init'         : 0x20000000 + 0x05,   # if your data alg's Init was at +0x05 (adjust if needed)
    'pc_unInit'       : 0x20000000 + 0x1b,
    'pc_program_page' : 0x20000000 + 0x3d,
    'pc_erase_sector' : 0x20000000 + 0x1f,
    'pc_eraseAll'     : 0xFFFFFFFF,

    'static_base'  : 0x20000000 + 0x4 + 0xcc,   # unchanged (0x200000d0)
    'begin_data'   : 0x20002000,                # page buffers start well above Zephyr usage
    'page_buffers' : [
        0x20002000,   # buffer0
        0x20002400,   # buffer1
    ],
    # buffers occupy up to 0x200027FF -> place stack bottom just above
    'end_stack'    : 0x20002800,
    'begin_stack'  : 0x20010000,                # top of SRAM (64 KiB device)

    'page_size'            : 0x40,
    'min_program_length'   : 0x40,

    'analyzer_supported' : False,
    'analyzer_address'   : 0x00000000,

    'ro_start' : 0x4,
    'ro_size'  : 0x88,
    'rw_start' : 0x8c,
    'rw_size'  : 0x8,
    'zi_start' : 0x94,
    'zi_size'  : 0x0,

    'flash_start' : 0x00400000,
    'flash_size'  : 0x00002000,
    'sector_sizes': ((0x0, 0x100),),
}
'''

'''
# RAM overflow for the first time
MAIN_FLASH_ALGO = {
    'load_address': 0x20000000,

    'instructions': [
        0xe7fdbe00,
        0x074a492d, 0x4a2e6011, 0x6051492c, 0x4449492d, 0x20006008,
        0x20004770, 0x210f4770, 0x400103c9, 0x200f0842, 0x40020380,
        0x4825b510, 0x4a2661c2, 0x69428002, 0xd0fc07d2, 0x22014c23,
        0x03d23c3f, 0xe00c188b, 0x61c2084a, 0x69428004, 0xd0fc07d2,
        0x07926942, 0x2001d501, 0x31ffbd10, 0x42993101, 0x2000d3f0,
        0xb5f0bd10, 0x08891cc9, 0x00894b16, 0x1cdb4d13, 0x696b802b,
        0xd0fc07db, 0x3e3d4e12, 0xd0162900, 0x29404603, 0x2440d901,
        0x460ce005, 0xca80e003, 0xc3801f09, 0x2c001f24, 0x802ed1f9,
        0x696b3040, 0xd0fc07db, 0x079b696b, 0x2001d5e8, 0x2000bdf0,
        0x0000bdf0, 0x00010022, 0x0004009e, 0x41004000, 0x00000004,
        0x0000a541, 0x00000000, 0x00000000
    ],

    # Function entry points (SRAM-relative)
    'pc_init'         : 0x20000005,
    'pc_unInit'       : 0x2000001b,
    'pc_program_page' : 0x2000006b,
    'pc_erase_sector' : 0x2000001f,
    'pc_eraseAll'     : 0xFFFFFFFF,  # no mass erase in this blob

    # # SRAM layout
    # 'static_base' : 0x20000000 + 0x4 + 0xcc,
    # 'begin_stack' : 0x200018e0,
    # 'end_stack'   : 0x200008e0,

    # # IMPORTANT: data begins at the first page buffer
    # 'begin_data'  : 0x200000e0,

    # # Programming granularity (matches FLM szPage)
    # 'page_size'            : 0x400,      # 1024 bytes per ProgramPage
    # 'min_program_length'   : 0x400,

    # # Double-buffering (each >= page_size)
    # 'page_buffers' : [
    #     0x200000e0,
    #     0x200004e0,
    # ],

    # SRAM layout — corrected to give 8 KiB stack to the flash algorithm
    'static_base' : 0x20000000 + 0x4 + 0xcc,
    # 'begin_stack' : 0x200088e0,   # 0x200088e0 - 0x200008e0 = 0x8000 = 32 KiB
    # 'begin_stack' : 0x20010000, # 0x20010000 - 0x200008e0 = 0x8000 = 64 KiB
    'begin_stack' : 0x2000C8E0, # 0x2000C8E0 - 0x200008e0 = 0x8000 = 48 KiB Arun
    'end_stack'   : 0x200008e0,   # keep the same lower bound

    # IMPORTANT: data begins at the first page buffer
    'begin_data'  : 0x200000e0,

    # Programming granularity (matches FLM szPage)
    'page_size'            : 0x400,      # 1024 bytes per ProgramPage
    'min_program_length'   : 0x400,

    # Double-buffering (each >= page_size)
    'page_buffers' : [
        0x200000e0,
        0x200004e0,
    ],

    'analyzer_supported' : False,
    'analyzer_address'   : 0x00000000,

    # Image layout within algo image
    'ro_start' : 0x4,
    'ro_size'  : 0xcc,
    'rw_start' : 0xd0,
    'rw_size'  : 0x8,
    'zi_start' : 0xd8,
    'zi_size'  : 0x0,

    # Flash geometry (used by pyOCD planner)
    'flash_start' : 0x00000000,
    'flash_size'  : 0x00080000,         # 512 KiB

    # The algo's EraseSector actually erases a **region** (32 KiB):
    'sector_sizes': (
        (0x0, 0x8000),                  # 32 KiB regions
    ),
}

DATA_FLASH_ALGO = {
    'load_address' : 0x20000000,

    'instructions': [
        0xe7fdbe00,
        0x074a491c, 0x4a1d6011, 0x6051491b, 0x4449491c, 0x20006008,
        0x20004770, 0x08414770, 0x61c14817, 0x80014918, 0x07c96941,
        0x6940d0fc, 0xd5010780, 0x47702001, 0x47702000, 0x4c12b510,
        0x342a4b0f, 0x695c801c, 0xd0fc07e4, 0x08891cc9, 0xe0020089,
        0x1f09ca10, 0x2900c010, 0x480ad1fa, 0x80181c80, 0x07c06958,
        0x6958d0fc, 0xd5010780, 0xbd102001, 0xbd102000, 0x00010022,
        0x0004009e, 0x41004000, 0x00000004, 0x0000a51a, 0x00000000,
        0x00000000
    ],

    'pc_init'         : 0x20000005,
    'pc_unInit'       : 0x2000001b,
    'pc_program_page' : 0x2000003d,
    'pc_erase_sector' : 0x2000001f,
    'pc_eraseAll'     : 0xFFFFFFFF,

    # 'static_base' : 0x20000000 + 0x4 + 0x88,
    # 'begin_stack' : 0x20001120,
    # 'end_stack'   : 0x20000120,

    # # IMPORTANT: data begins at the first page buffer
    # 'begin_data'  : 0x200000a0,

    # 'page_size'            : 0x40,       # 64 bytes per ProgramPage (data flash)
    # 'min_program_length'   : 0x40,

    # 'page_buffers' : [
    #     0x200000a0,
    #     0x200000e0,
    # ],

    'static_base' : 0x20000000 + 0x4 + 0x88,

    # 16 KiB stack region
    'begin_stack' : 0x20004120,   # new top of stack
    'end_stack'   : 0x20000120,   # bottom of stack

    # Data buffers
    'begin_data'  : 0x200000a0,

    'page_size'            : 0x40,       # 64 bytes per ProgramPage
    'min_program_length'   : 0x40,

    'page_buffers' : [
        0x200000a0,
        0x200000e0,
    ],

    'analyzer_supported' : False,
    'analyzer_address'   : 0x00000000,

    'ro_start' : 0x4,
    'ro_size'  : 0x88,
    'rw_start' : 0x8c,
    'rw_size'  : 0x8,
    'zi_start' : 0x94,
    'zi_size'  : 0x0,

    'flash_start' : 0x00400000,
    'flash_size'  : 0x00002000,          # 8 KiB data flash

    # Data flash erase granularity is a **row** = 256 bytes
    'sector_sizes': (
        (0x0, 0x100),                    # 256 B rows
    ),
}
'''

# From DFP
MAIN_FLASH_ALGO = {
    'load_address' : 0x20000000,

    # Flash algorithm as a hex string
    'instructions': [
    0xe7fdbe00,
    0x074a492d, 0x4a2e6011, 0x6051492c, 0x4449492d, 0x20006008, 0x20004770, 0x210f4770, 0x400103c9,
    0x200f0842, 0x40020380, 0x4825b510, 0x4a2661c2, 0x69428002, 0xd0fc07d2, 0x22014c23, 0x03d23c3f,
    0xe00c188b, 0x61c2084a, 0x69428004, 0xd0fc07d2, 0x07926942, 0x2001d501, 0x31ffbd10, 0x42993101,
    0x2000d3f0, 0xb5f0bd10, 0x08891cc9, 0x00894b16, 0x1cdb4d13, 0x696b802b, 0xd0fc07db, 0x3e3d4e12,
    0xd0162900, 0x29404603, 0x2440d901, 0x460ce005, 0xca80e003, 0xc3801f09, 0x2c001f24, 0x802ed1f9,
    0x696b3040, 0xd0fc07db, 0x079b696b, 0x2001d5e8, 0x2000bdf0, 0x0000bdf0, 0x00010022, 0x0004009e,
    0x41004000, 0x00000004, 0x0000a541, 0x00000000, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x20000005,
    'pc_unInit': 0x2000001b,
    'pc_program_page': 0x2000006b,
    'pc_erase_sector': 0x2000001f,
    'pc_eraseAll': 0x120000003,

    'static_base' : 0x20000000 + 0x00000004 + 0x000000cc,
    'begin_stack' : 0x200018e0,
    'end_stack' : 0x200008e0,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x400,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x200000e0,
        0x200004e0
    ],
    'min_program_length' : 0x400,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0xcc,
    'rw_start': 0xd0,
    'rw_size': 0x8,
    'zi_start': 0xd8,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x0,
    'flash_size': 0x80000,
    'sector_sizes': (
        (0x0, 0x8000),
    )
}

DATA_FLASH_ALGO = {
    'load_address' : 0x20000000,

    # Flash algorithm as a hex string
    'instructions': [
    0xe7fdbe00,
    0x074a491c, 0x4a1d6011, 0x6051491b, 0x4449491c, 0x20006008, 0x20004770, 0x08414770, 0x61c14817,
    0x80014918, 0x07c96941, 0x6940d0fc, 0xd5010780, 0x47702001, 0x47702000, 0x4c12b510, 0x342a4b0f,
    0x695c801c, 0xd0fc07e4, 0x08891cc9, 0xe0020089, 0x1f09ca10, 0x2900c010, 0x480ad1fa, 0x80181c80,
    0x07c06958, 0x6958d0fc, 0xd5010780, 0xbd102001, 0xbd102000, 0x00010022, 0x0004009e, 0x41004000,
    0x00000004, 0x0000a51a, 0x00000000, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x20000005,
    'pc_unInit': 0x2000001b,
    'pc_program_page': 0x2000003d,
    'pc_erase_sector': 0x2000001f,
    'pc_eraseAll': 0x120000003,

    'static_base' : 0x20000000 + 0x00000004 + 0x00000088,
    'begin_stack' : 0x20001120,
    'end_stack' : 0x20000120,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x40,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    # Enable double buffering
    'page_buffers' : [
        0x200000a0,
        0x200000e0
    ],
    'min_program_length' : 0x40,

    # Relative region addresses and sizes
    'ro_start': 0x4,
    'ro_size': 0x88,
    'rw_start': 0x8c,
    'rw_size': 0x8,
    'zi_start': 0x94,
    'zi_size': 0x0,

    # Flash information
    'flash_start': 0x400000,
    'flash_size': 0x2000,
    'sector_sizes': (
        (0x0, 0x100),
    )
}


class PIC32CM5164JH01100(CoreSightTarget):
    VENDOR = "Microchip"

    MEMORY_MAP = MemoryMap(
        # Use erase block size that matches EraseSector() behavior
        FlashRegion(start=0x00000000, length=0x00080000, blocksize=0x8000,
                    is_boot_memory=True, algo=MAIN_FLASH_ALGO),

        FlashRegion(start=0x00400000, length=0x00002000, blocksize=0x100,
                    is_boot_memory=False, algo=DATA_FLASH_ALGO),

        # User row is not writable with these algos; leave as memory-only
        MemoryRegion(start=0x00804000, length=0x200, name="user_row",
                     is_flash=False, is_ram=False),

        RamRegion(start=0x20000000, length=64 * 1024),
    )

    def __init__(self, session):
        super().__init__(session, self.MEMORY_MAP)
