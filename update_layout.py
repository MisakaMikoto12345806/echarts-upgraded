#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read the original HTML file
with open(r'D:\yatengstudy\echarts123\echarts-upgraded\app\templates\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old section to replace
old_section = '''    <!-- Main Content -->
    <main class="flex-grow px-0 py-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-0 mb-6 h-auto">
            <!-- 左列: 各国学校数量、学科开设情况统计 -->
            <div class="flex flex-col h-full">
                <!-- 各国学校数量 -->
                <div class="chart-container p-4 flex-grow">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-globe-asia mr-2"></i>各国学校数量
                    </h2>
                    <div id="country-pie-chart" class="h-80"></div>
                </div>

                <!-- 学科开设情况统计 -->
                <div class="chart-container p-4 flex-grow mt-6">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-bullseye mr-2"></i>学科开设情况统计
                    </h2>
                    <div id="bubble-chart" class="h-96"></div>
                </div>
            </div>

            <!-- 右列: 学费统计情况、学校存在时间统计 -->
            <div class="flex flex-col h-full">
                <!-- 学费统计情况 -->
                <div class="chart-container p-4 flex-grow">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-money-bill-wave mr-2"></i>学费统计情况
                    </h2>
                    <div id="tuition-bar-chart" class="h-80"></div>
                </div>

                <!-- 学校存在时间统计 -->
                <div class="chart-container p-4 flex-grow mt-6">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-chart-line mr-2"></i>学校存在时间统计
                    </h2>
                    <div id="timeline-chart" class="h-80"></div>
                </div>
            </div>
        </div>
    </main>'''

# Define the new section
new_section = '''    <!-- Main Content -->
    <main class="flex-grow px-0 py-6">
        <div class="flex flex-col lg:flex-row justify-between items-start gap-8 px-6">
            <!-- 左侧组: 各国学校数量、学科开设情况统计 -->
            <div class="w-full lg:w-2/5 flex flex-col h-full">
                <!-- 各国学校数量 -->
                <div class="chart-container p-4 flex-grow mb-6">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-globe-asia mr-2"></i>各国学校数量
                    </h2>
                    <div id="country-pie-chart" class="h-80"></div>
                </div>

                <!-- 学科开设情况统计 -->
                <div class="chart-container p-4 flex-grow">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-bullseye mr-2"></i>学科开设情况统计
                    </h2>
                    <div id="bubble-chart" class="h-96"></div>
                </div>
            </div>

            <!-- 右侧组: 学费统计情况、学校存在时间统计 -->
            <div class="w-full lg:w-2/5 flex flex-col h-full">
                <!-- 学费统计情况 -->
                <div class="chart-container p-4 flex-grow mb-6">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-money-bill-wave mr-2"></i>学费统计情况
                    </h2>
                    <div id="tuition-bar-chart" class="h-80"></div>
                </div>

                <!-- 学校存在时间统计 -->
                <div class="chart-container p-4 flex-grow">
                    <div class="bottom-corner"></div>
                    <h2 class="text-xl font-semibold text-center mb-4 chart-title">
                        <i class="fas fa-chart-line mr-2"></i>学校存在时间统计
                    </h2>
                    <div id="timeline-chart" class="h-80"></div>
                </div>
            </div>
        </div>
    </main>'''

# Replace the old section with the new section
updated_content = content.replace(old_section, new_section)

# Write the updated content back to the file
with open(r'D:\yatengstudy\echarts123\echarts-upgraded\app\templates\index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Successfully updated the index.html file with the new layout!")