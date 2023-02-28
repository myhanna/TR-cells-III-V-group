# ! /bin/bash

mpirun -np 16 pw.x < GaSb.scf.in > GaSb.scf.out
mpirun -np 16 pw.x < GaSb.nscfband.in > GaSb.nscfband.out
mpirun -np 16 bands.x < GaSb.band.in > GaSb.band.out
rm -rf ./work/   