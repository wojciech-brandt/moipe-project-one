clc
clear

axes = readmatrix("main_for_matlab");
data = readmatrix("nonstandarised.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "wielomiany", figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(axes(1,:), data(1,:), 'k-')
plot(axes(1,:), data(2,:), 'b-')
plot(axes(1,:), data(3,:), 'Color', '#77AC30', 'LineStyle', '-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f2 = figure('Name', 'logarytm', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(axes(1,:), data(5,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f3 = figure('Name', 'wymierna', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(axes(1,:), data(6,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");

f4 = figure('Name', 'trigi', figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(axes(1,:), data(4,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");