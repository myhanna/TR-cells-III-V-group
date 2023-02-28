# ! /bin/bash

mpirun -np 36 pw.x < GaSb.scf.in > GaSb.scf.out
mpirun -np 36 pw.x < GaSb.nscf.in > GaSb.nscf.out
mpirun -np 36 epsilon.x < GaSb.epsilon.in > GaSb.epsilon.out
mpirun -np 36 epsilon.x < GaSb.jdos.in > GaSb.jdos.out
    