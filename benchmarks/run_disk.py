# run disk benchmark and plot a figure
import matplotlib.pyplot as plt
import numpy
from benchmark_disk import run_gmsh, run_SeismicMesh, run_cgal


plt.rcParams.update({"font.size": 18})


colors1 = ["ko-", "ro-", "bo-"]
colors2 = ["ko--", "ro--", "bo--"]
labels = ["gmsh", "SeismicMesh", "cgal"]

entries = []
# minimize mesh size
rg = numpy.linspace(0.1, 0.01, 10)
for i, func in enumerate([run_gmsh, run_SeismicMesh, run_cgal]):
    q = []
    mq = []
    nv = []
    nc = []
    t = []

    for hmin in rg:
        quality, elapsed, num_vertices, num_cells = func(HMIN=hmin)
        q.append(numpy.mean(quality))
        mq.append(numpy.min(quality))
        t.append(elapsed)
        nv.append(num_vertices)
        nc.append(num_cells)

    plt.subplot(1, 2, 1)
    h = plt.plot(nc, t, colors1[i], label=labels[i])

    plt.subplot(1, 2, 2)
    plt.plot(nc, q, colors1[i])
    plt.plot(nc, mq, colors2[i])
    entries.append(h)

plt.subplot(1, 2, 1)
plt.title("Number of cells vs. mesh generation time")
plt.legend()
plt.xlabel("Number of cells")
plt.ylabel("Elapsed time (s)")
plt.grid()

plt.subplot(1, 2, 2)
plt.title("Number of cells. vs cell quality")
plt.xlabel("Number of cells")
plt.ylabel("Cell quality")
plt.grid()

plt.show()
