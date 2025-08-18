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
