# CuValley HACK

The solution of the CuValley HACK task 2 - "Stabilizacja pracy pieca zawiesinowego" developed by [HARDCODED](https://github.com/HARDCODED-PL) team.

## Contributors

- [MatPiech](https://github.com/MatPiech)
- [Ciasterix](https://github.com/Ciasterix)
- [bartoszptak](https://github.com/bartoszptak)
- [krigaree](https://github.com/krigaree)

## Task

The main aim of the project was to develop an empirical model of flash smelting furnace control in order to stabilize its work in the area of heat extraction (stabilization of the amount of extracted SR heat).

## Approach

<p align="center">
  <img width="460" height="300" src="https://github.com/HARDCODED-PL/CuValley/blob/main/data/stanet.png">
</p>

StaNet is a LightGBM based model which is responsible for preparing flash smelting furnace manipulable variables. It consists of 2 blocks:

- controller block - predicting variables,
- stabilizer block - variables checking with constrains and smoothing.

The model takes as input three parameters:

- disturbing variables from current timestamp,
- disturbed variables from previous timestamp,
- manipulable variables from previous timestamp.

As a result model return manipulable variables for current timestamp.

<p align="center">
  <img width="460" height="300" src="https://github.com/HARDCODED-PL/CuValley/blob/main/data/stanet_graph.png">
</p>

## Control parameters

Simulation configuration parameters are predefined and easily changeable in [config.yaml](./config.yaml) file.

```yaml
environment:
  hmg_model: './models/hmg.pkl'
  disturbed_variables_model: './models/disturbed_variables_model.pkl'

regulator:
  controller_model: './models/dummy_operator.pkl'

  constraints:
    air_flow:
      air_max_regulation: [1900, 3500]
      air_max_step: 80 # 800
      air_min_time: 1 # 10
    oxygen_content:
      oxy_max_regulation: [65, 81]
      oxy_max_step: 0.8 # 2
      oxy_min_time: 60 # 150
    air_blow:
      puff_max_regulation: [40, 70]
      puff_max_step: 2 # 10
      puff_min_time: 1 # 5
    dust:
      dust_max_regulation: [13, 27]
      dust_max_step: 13
      dust_min_time: 300

```

## Results

<center>

| Metryki 	| Dane rzeczywiste 	| StaNet 	|
|:-:	|:-:	|:-:	|
| Odchylenie standardowe 	| 1.929 	| 0.833 	|
| Wariancja 	| 3.721 	| 0.694 	|
| Rozstęp 	| 16.418 	| 8.364 	|

</center>

<p align="center">
  <img width="460" height="300" src="https://github.com/HARDCODED-PL/CuValley/blob/main/data/stabilized_results.png">
</p>
