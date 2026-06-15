# Buffer Overflow Attack

[![C](https://img.shields.io/badge/C-stack%20smashing-A8B9CC?logo=c&logoColor=black)](https://en.wikipedia.org/wiki/Stack_buffer_overflow)
[![Python](https://img.shields.io/badge/Python-exploit%20builder-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Platform](https://img.shields.io/badge/platform-Linux%2032--bit-orange)
![Scope](https://img.shields.io/badge/scope-educational-blue)

A classic **stack buffer overflow** that hijacks a vulnerable Set-UID root
program and spins up a **root shell** — the textbook "smashing the stack"
attack, built end to end. Based on the [SEED Labs](https://seedsecuritylabs.org/)
buffer-overflow project.

> **Educational only.** This runs against a deliberately vulnerable program in an
> isolated SEED Labs VM (32-bit, ASLR off, no stack canaries, executable stack).
> It exists to teach how the attack — and the defenses against it — actually work.

## The idea in one picture

```
   badfile (517 bytes)
   ┌──────────────────────────────────────────────┐
   │ NOP sled (0x90...) │ return addr │ ... │ shellcode │
   └──────────────────────────────────────────────┘
                              │
        bof() does strcpy(buffer, str)  ← no bounds check
                              │
        overwrites the saved return address ▼
                  jumps into the NOP sled ──► shellcode ──► /bin/sh (as root)
```

The vulnerable program ([`stack.c`](src/stack.c)) copies attacker-controlled
input into an undersized stack buffer with `strcpy`. By crafting the input so the
overwritten **return address** points back into a NOP sled leading to injected
**shellcode**, control flow lands on code that calls `execve("/bin/sh")`. Because
the program is Set-UID root, that shell runs as root.

## How it works

- [`exploit.py`](src/exploit.py) — builds `badfile`: a 517-byte payload of a NOP
  sled, the shellcode (an `execve("/bin/sh")` stub), and the computed return
  address placed at the right stack offset.
- [`stack.c`](src/stack.c) — the vulnerable target; `bof()` overflows a
  fixed-size buffer via `strcpy`.
- [`call_shellcode.c`](src/call_shellcode.c) — sanity check that the raw
  shellcode spawns a shell on its own.
- [`set_uid_root.c`](src/set_uid_root.c) — minimal Set-UID demonstration helper.
- [`attack.sh`](src/attack.sh) / [`reset.sh`](src/reset.sh) — run and clean up.

## Running it (SEED Labs VM)

```bash
cd src
bash attack.sh     # compiles stack.c, makes it Set-UID root, builds badfile, runs it
# you should land in a shell:
id                 # uid=1000(seed) gid=1000(seed) euid=0(root) ...

bash reset.sh      # remove generated badfile + binary
```

`attack.sh` compiles with the lab's required flags
(`-z execstack -fno-stack-protector`) and sets the Set-UID root bit before
triggering the overflow.

## Key parameters

The two numbers that make or break the exploit live in `exploit.py`:

- **`offset`** — distance from the buffer to the saved return address (`152` here).
- **`ret`** — the address to jump to, landing inside the NOP sled.

These are specific to this build/VM; SEED randomizes the buffer size per term, so
they're derived by inspecting the stack layout in a debugger.

See [`docs/report.pdf`](docs/report.pdf) for the full write-up, including how the
offset and return address were found.
