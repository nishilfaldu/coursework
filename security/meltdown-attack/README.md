# Meltdown Attack

[![C](https://img.shields.io/badge/C-side%20channel-A8B9CC?logo=c&logoColor=black)](https://meltdownattack.com/)
[![Linux Kernel](https://img.shields.io/badge/Linux-kernel%20module-FCC624?logo=linux&logoColor=black)](https://www.kernel.org/)
![CVE](https://img.shields.io/badge/CVE--2017--5754-Meltdown-red)
![Scope](https://img.shields.io/badge/scope-educational-blue)

A hands-on implementation of **Meltdown** ([CVE-2017-5754](https://nvd.nist.gov/vuln/detail/CVE-2017-5754))
— the 2018 hardware vulnerability that let user programs read **kernel memory**
they should never be able to touch, by exploiting out-of-order execution and a
cache **timing side channel**. Based on the [SEED Labs](https://seedsecuritylabs.org/)
Meltdown project.

> **Educational only.** Runs in an isolated SEED Labs VM on vulnerable hardware.
> A companion kernel module deliberately stashes a "secret" in kernel space so we
> can try to steal it from user space — purely to understand the attack.

## How Meltdown works

The CPU, racing ahead with out-of-order execution, *speculatively* reads a
forbidden kernel byte before the permission check fails. The read result is
discarded — but it leaves a footprint in the **CPU cache**. We then measure
access times across a probing array to figure out which value was cached, and
thereby recover the secret byte. One byte at a time, kernel memory leaks out.

```
speculative read of kernel byte  ──►  touches array[secret * 4096]
                │                                   │
        exception (discarded)              leaves a cache trace
                                                    │
        FLUSH+RELOAD timing  ◄──────────────  fastest index == secret
```

## Built up step by step

The SEED lab develops the attack as a progression of small experiments, each
implemented here:

| File | What it demonstrates |
|------|----------------------|
| [`CacheTime.c`](src/CacheTime.c) | Cached vs. uncached memory is measurably faster to read |
| [`FlushReload.c`](src/FlushReload.c) | The FLUSH+RELOAD side channel: recover a value purely from timing |
| [`ExceptionHandling.c`](src/ExceptionHandling.c) | Survive the illegal kernel access via a `SIGSEGV` handler (`sigsetjmp`/`siglongjmp`) |
| [`MeltdownKernel.c`](src/MeltdownKernel.c) | Kernel module that places a secret at a known kernel address |
| [`MeltdownExperiment.c`](src/MeltdownExperiment.c) | The full attack: speculative read + side-channel recovery |
| [`GuardTest.c`](src/GuardTest.c) | Supporting experiment on access boundaries |

## Running it (SEED Labs VM)

```bash
cd src

# 1) Build and load the kernel module that holds the secret
make
sudo insmod MeltdownKernel.ko
# find the secret's kernel address in the log:
dmesg | grep 'secret data address'

# 2) Put that address into MeltdownExperiment.c (the meltdown_asm(...) call),
#    then build and run the attack
gcc -march=native -o meltdown MeltdownExperiment.c
./meltdown

# 3) Unload when done
sudo rmmod MeltdownKernel
```

The kernel address is machine-specific, so it's read from `dmesg` and pasted into
the experiment before compiling.

See [`docs/report.pdf`](docs/report.pdf) for the full write-up, including timing
thresholds, reliability tuning, and observations across the experiments.
