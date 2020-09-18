# theta_gates_reliable_sequences_mEC
Helper files and libraries used for simulations

## Usage
The code in this repository uses a C++ library (insilico) to simulate single and networks of conductance based neurons. To run the simulations follow the steps listed below.
### Step 1 - Download insilico
See README.md in https://github.com/CollinsAssisi/insilico for installing this library
Each subfolder in this repository contains a seperate insilico folder with all the header files necessary for running the simulations.

### Step 2 - Interfacing python with insilico
Python and bash in linux are used to generate the helper files (files with suffix .nsets holds neuron parameters, files with suffix .ssets holds synapse parameters) required for insilico and to compile and run the simulations. 

### Step 2a
Follow the notebook How_To_Neuron to get a sense of how to use insilico + python to run a simulation of a single neuron
### Step 2b
Follow the notebook How_To_Network to get a sense of how to use insilico + python to run a simulation of synaptically coupled neurons

## Step 3 -  Steps to generate figures

*Fig 1.*

0. enter into the folder "I2E2"

1. Generate the helper files (nsets, ssets)

```bash
python scripts/gen_nsets_I2E2_autonomous.py
python scripts/gen_nsets_I2E2_autonomous.py
python scripts/gen_ssets_I2E2.py
```

2. Compile the main cpp file which has specifications for the number of neurons, neuron types, number of synapses, synapse types and so on.

```bash
./scripts/compilemany_I2E2_autonomous.sh
./scripts/compilemany_I2E2_toggle.sh
```

3. Run the simulation

```bash
python scripts/run_a_I2E2_switching_autonomous.py
pyton scripts/run_a_I2E2_switching_toggle.py
```

After the simulation is over, the outputs would have been stored in the folder dir_output.
use the accompanying plotting script to produce a figure similar to Fig.1.

```bash
python scripts/plot_data.py <dir_output/filename.dat>
```

*Fig 2. & Fig 4. - Theta vs. No Theta in a larger network*

0. enter into the folder I40E40
1. Generate the helper files (nsets, ssets)

```bash
python scripts/gen_nsets_I40E40_shorterPulse.py	
python scripts/gen_ssets_I40E40_randomEtoI_without_replacement.py
```

2. Compile the main cpp file with specifications for the number of neurons, neuron types, number of synapses, synapse types and so on.

```bash
./scripts/compile_many_I40E40_variablePulse.sh
```

3. run the simulation

```bash
python scripts/run_a_I40E40_randomei.py
```

4. Calculate the spike times

```bash
python scripts/calc_spike_times.py
```

5. produce the raster plots

```bash
python scripts/plot_raster.py
```


6. 	   




