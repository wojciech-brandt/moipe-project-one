clc
clear

axes = readmatrix("main_for_matlab.csv");
zag_axes = readmatrix("N_main_for_matlab.csv");
data = readmatrix("standarised.csv");
zag_data = readmatrix("N_standarised.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "wielomiany", figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(zag_axes(2,:), zag_data(1,:), 'k-')
plot(zag_axes(2,:), zag_data(2,:), 'b-')
plot(zag_axes(2,:), zag_data(3,:), 'Color', '#77AC30', 'LineStyle', '-')
grid;
xlabel("zmienna standaryzowana");
ylabel("temperatura [°C]");

f3 = figure('Name', 'wymierna', figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(zag_axes(2,:), zag_data(5,:), 'b-')
grid;
xlabel("zmienna standaryzowana");
ylabel("temperatura [°C]");

f4 = figure('Name', 'trigi', figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(zag_axes(2,:), zag_data(4,:), 'b-')
grid;
xlabel("zmienna standaryzowana");
ylabel("temperatura [°C]");

