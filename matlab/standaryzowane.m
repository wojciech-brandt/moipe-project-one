clc
clear

axes = readmatrix("main_for_matlab");
data = readmatrix("standarised.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "wielomiany", figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(axes(2,:), data(1,:), 'k-')
plot(axes(2,:), data(2,:), 'b-')
plot(axes(2,:), data(3,:), 'Color', '#77AC30', 'LineStyle', '-')
grid;
xlabel("zmienna standaryzowana");
ylabel("napięcie [V]");

f3 = figure('Name', 'wymierna', figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(axes(2,:), data(5,:), 'b-')
grid;
xlabel("zmienna standaryzowana");
ylabel("napięcie [V]");

f4 = figure('Name', 'trigi', figOpt{:});
plot(axes(2,:), axes(3,:), 'r*')
hold on
plot(axes(2,:), data(4,:), 'b-')
grid;
xlabel("zmienna standaryzowana");
ylabel("napięcie [V]");
