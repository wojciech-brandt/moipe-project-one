clc
clear

axes = readmatrix("main_for_matlab.csv");
zag_axes = readmatrix("N_main_for_matlab.csv");
data = readmatrix("nonstandarised.csv");
zag_data = readmatrix("N_nonstandarised.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "wielomiany", figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(zag_axes(1,:), zag_data(1,:), 'k-')
plot(zag_axes(1,:), zag_data(2,:), 'b-')
plot(zag_axes(1,:), zag_data(3,:), 'Color', '#77AC30', 'LineStyle', '-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f2 = figure('Name', 'logarytm', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(zag_axes(1,:), zag_data(5,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f3 = figure('Name', 'wymierna', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(zag_axes(1,:), zag_data(6,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f4 = figure('Name', 'trigi', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(zag_axes(1,:), zag_data(4,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");