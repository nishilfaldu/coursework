"use client";
import { Carousel, Tabs } from "antd";
import { data, users } from "../../../lib/data/children";
import { Slide } from "./Slide";

const descriptions = [
  {
    label: "Purpose",
    key: "1",
    children:
      "The main purpose of this visualization is to analyze and present insights on the demographics, poses, features, and moods of people taking selfies in different urban environments.",
  },
  {
    label: "Data and Collection",
    key: "2",
    children: data,
  },
  {
    label: "Users",
    key: "4",
    children: users,
  },
  {
    label: "Q&A",
    key: "5",
    children: (
      <div>
        <h4 className="font-bold">
          Are there differences in selfie poses between cities or cultures?
        </h4>
        <p>
          The tool likely includes filters or comparisons by city, which would
          allow users to see variations in head tilt, gaze direction, and other
          pose attributes across different locations.
        </p>

        <h4 className="font-bold mt-2">
          Does age affect how people take selfies?
        </h4>
        <p>
          If age data is available, users could look for patterns in the age
          distribution graph and correlate that with other features, like pose
          or expression, to see if certain age groups prefer specific selfie
          styles.
        </p>

        <h4 className="font-bold mt-2">
          How do gender and expression correlate in selfies?
        </h4>
        <p>
          The visualization probably offers ways to cross-reference gender data
          with mood or facial features (like smiling), enabling users to explore
          gendered expressions in selfies.
        </p>

        <h4 className="font-bold mt-2">
          What time of day or in what settings are people more likely to take
          selfies?
        </h4>
        <p>
          While this may not be directly visualized, if the dataset includes
          timestamps or location settings (like indoors vs. outdoors), users
          could infer this information.
        </p>

        <h4 className="font-bold mt-2">
          How has the trend of taking selfies evolved over time?
        </h4>
        <p>
          If the dataset spans a significant timeframe, users might be able to
          observe trends and see how selfie styles have changed.
        </p>

        <h4 className="font-bold mt-2">
          Do people in certain cities prefer to take more expressive selfies?
        </h4>
        <p>
          By examining the mood analysis for different cities, users can see if
          some locales have a higher prevalence of happy or calm expressions.
        </p>

        <h4 className="font-bold mt-2">
          What selfie-related trends could be interesting for marketers?
        </h4>
        <p>
          Marketers could analyze the features section to understand popular
          trends in accessories (like glasses) or facial expressions and apply
          these insights to advertising campaigns.
        </p>
      </div>
    ),
  },
  {
    label: "Insights",
    key: "7",
    children: (
      <div>
        <p>
          To find answers within the Selfiecity interface, users would interact
          with the visualization tools provided. These might include:
        </p>

        <ul>
          <li>
            <strong>Mood:</strong> This chart categorizes the selfies by mood:
            calm, angry, and happy. There is an additional label for not-happy
            under the happy mood, indicating a possible subcategory or an error
            in the image.
          </li>
          <li>
            <strong>Glasses:</strong> This visualization shows the distribution
            of selfies with or without glasses, making it easy to observe the
            prevalence of either attribute in the dataset.
          </li>
          <li>
            <strong>Mouth:</strong> Here, selfies are categorized by whether the
            persons mouth is open or closed, providing insights into common
            facial expressions.
          </li>
          <li>
            <strong>Eyes:</strong> This chart does a similar categorization for
            the eyes, showing the proportion of selfies where the persons eyes
            are open or closed.
          </li>
          <li>
            <strong>Tilt:</strong> This graph displays the head tilt in the
            selfies, showing a distribution that could indicate a common pose or
            a preferred side.
          </li>
          <li>
            <strong>Turn:</strong> Similarly, this visualization illustrates the
            direction people turn their heads when taking selfies, indicating
            the profile orientation.
          </li>
          <li>
            <strong>Pose:</strong> The chart here represents the overall head
            position, whether people tend to look up, straight, or down in their
            selfies.
          </li>
          <li>
            <strong>Age and Gender:</strong> This shows the average age and
            gender distribution of the selfie-takers. A highlighted point shows
            an average age, in this case, 24.2 years.
          </li>
          <li>
            <strong>City:</strong> The final image puts the data in the
            geographic context, highlighting New York City on a world map,
            indicating that the dataset is likely filtered to show only selfies
            from this city.
          </li>
        </ul>

        <p>
          Users can interact with these visualizations by clicking, drag and
          drop and brushing to ask and answer questions about selfie trends and
          characteristics within the population of New York City. The interface
          presumably allows users to filter and drill down into specific subsets
          of the data, compare between different categories, and perhaps switch
          to different cities for comparative analysis.
        </p>
      </div>
    ),
  },
  {
    label: "Design Choices",
    key: "8",
    children: (
      <div>
        <p>
          The design choices in the Selfiecity projects visualizations use
          several effective techniques to present the complex data in an
          accessible and engaging way:
        </p>
        <ul>
          <li>
            <strong>Color Contrast and Consistency:</strong> The use of a dark
            background with lighter foreground elements makes the charts easy to
            read. Consistent use of color coding helps users quickly associate
            certain colors with specific data points across different
            visualizations.
          </li>

          <li>
            <strong>Segmented Data Visualization:</strong> Categorizing data
            into clear segments, such as mood, allows for quick comparison and
            easier understanding of proportions within the data set.
          </li>

          <li>
            <strong>Infographics Style:</strong> Using easily recognizable icons
            and clear labels (such as the symbols for glasses, gender, and the
            mood faces) makes the information understandable at a glance.
          </li>

          <li>
            <strong>Interactive Elements:</strong> While not visible in the
            screenshots, interactive elements that allow users to hover over or
            click on parts of the data for more detailed information can
            significantly enhance user engagement and understanding.
          </li>

          <li>
            <strong>Statistical Averages:</strong> Highlighting statistical
            averages, like the average age of selfie takers, provides a
            reference point that users can easily interpret and compare against
            other data points.
          </li>

          <li>
            <strong>Geographic Contextualization:</strong> Including a map with
            a highlighted area gives geographical context to the data, allowing
            users to understand the regional focus of the data set.
          </li>

          <li>
            <strong>Data Distribution Visuals:</strong> Histograms and other
            distribution charts effectively communicate the spread of data, such
            as age range and head tilt tendencies.
          </li>

          <li>
            <strong>Scale and Proportion:</strong> The proportional
            representation of data points, like the size difference between the
            YES and NO circles for glasses, offers an intuitive grasp of
            quantitative differences.
          </li>
        </ul>

        <p>
          These design choices help make complex datasets more accessible to a
          broader audience and can assist users in making data-driven inferences
          and conclusions. They also enable a level of data exploration that can
          accommodate both casual observers and professionals looking for
          detailed insights.
        </p>
      </div>
    ),
  },
  {
    label: "Limitations of Design",
    key: "9",
    children: (
      <div>
        <p>
          While the design choices in the Selfiecity projects visualizations
          offer several strengths, there are inherent limitations that may
          restrict a users ability to fully interact with and interpret the
          data:
        </p>

        <ol>
          <li>
            <strong>Static Images:</strong> If the visualizations are static
            images rather than interactive, it limits the users ability to
            explore the data dynamically. Users cannot click to get more
            information or see underlying data points.
          </li>

          <li>
            <strong>Limited Depth:</strong> The visualizations provide an
            overview but may not allow for drilling down into more granular
            data, such as the time of day the selfie was taken or the specific
            location within the city.
          </li>

          <li>
            <strong>No Temporal Data:</strong> The screenshots do not indicate
            changes over time, which means trends and changes in selfie behavior
            cannot be tracked or analyzed.
          </li>

          <li>
            <strong>Categorical Ambiguity:</strong> Without a clear legend or
            interactive tooltips, the meaning of certain categories may be
            ambiguous. For example, not-happy under the Happy mood category is
            unclear.
          </li>

          <li>
            <strong>Data Source and Sampling:</strong> There is no indication of
            the source of the selfies or the methodology used for sampling them,
            which raises questions about data representativeness and bias.
          </li>

          <li>
            <strong>Comparative Limitations:</strong> Without being able to
            overlay or directly compare different data sets (e.g., comparing
            mood across different cities), insights are limited to within the
            specific dataset shown.
          </li>

          <li>
            <strong>Quantitative Analysis:</strong> The lack of numerical labels
            or scales makes it difficult to make precise comparisons or to
            understand the actual numbers or percentages represented by the
            visual elements.
          </li>

          <li>
            <strong>Overlooking Diversity:</strong> Aggregate data can often
            overshadow the diversity within categories. For instance, gender
            might be presented as binary, which does not represent the full
            spectrum of gender identities.
          </li>

          <li>
            <strong>No Contextual Data:</strong> The visualizations do not
            include contextual data that could influence selfie styles, such as
            weather, events, or social context at the time the selfie was taken.
          </li>

          <li>
            <strong>Language and Accessibility:</strong> The use of English
            language for labels and instructions may limit understanding for
            non-English speakers, and the visual design may not be accessible to
            users with visual impairments.
          </li>
        </ol>

        <p>
          To overcome these limitations, a more interactive design with
          additional layers of data, dynamic querying capabilities, and more
          detailed metadata about the dataset and collection methodology would
          be required. This would allow users to gain a more nuanced
          understanding of the data and to perform a more comprehensive
          analysis.
        </p>
      </div>
    ),
  },
  {
    label: "Improvements",
    key: "10",
    children: (
      <div>
        <p>
          The design choices in the Selfiecity visualizations aim to present
          complex data clearly and engagingly, but there are areas where
          effectiveness may be lacking, which can be improved in several ways:
        </p>

        <ol>
          <li>
            <strong>Ambiguity in Categorization:</strong> As seen in the
            &apos;Mood&apos; chart with categories like &apos;Calm&apos;,
            &apos;Angry&apos;, and &apos;Happy&apos;, there&apos;s an ambiguous
            &apos;Not Happy&apos; label under &apos;Happy&apos;, which could
            confuse users. Clarifying these categories or providing a legend to
            explain the methodology behind mood categorization would improve
            understanding.
          </li>

          <li>
            <strong>Lack of Scale or Units:</strong> Some charts are missing
            axis labels or scales, which makes it difficult to quantify the
            visualized data. Adding clear scales and units would enable users to
            make more precise, data-driven observations and comparisons.
          </li>

          <li>
            <strong>Inconsistent Visual Encoding:</strong> In the
            &apos;Glasses&apos;, &apos;Mouth&apos;, and &apos;Eyes&apos; charts,
            it&apos;s not immediately clear why certain options are encircled
            while others are not, which could lead to misinterpretation. Using
            consistent visual encoding for similar types of data can improve
            comprehension.
          </li>

          <li>
            <strong>Data Overload:</strong> While it&apos;s important to provide
            comprehensive data, too much information in a single view can
            overwhelm users. Implementing a dashboard with the ability to toggle
            between different data sets or to filter data would help manage
            cognitive load.
          </li>

          <li>
            <strong>Interactive Elements:</strong> If the visualizations are
            static, users can&apos;t interact with the data to explore it
            further. Providing interactive elements such as hover-over details,
            clickable categories, and dynamic filtering could greatly enhance
            user engagement and insight discovery.
          </li>

          <li>
            <strong>Data Representation:</strong> In the pose data (such as
            &apos;Tilt&apos; and &apos;Turn&apos;), the visual metaphor used to
            represent the data may not be intuitive for all users. Simplifying
            these representations or providing a short explanatory text could
            make the data more accessible.
          </li>

          <li>
            <strong>Accessibility:</strong> For users with visual impairments,
            the contrast might be insufficient, and the reliance on color coding
            could be problematic for color-blind users. Ensuring high contrast
            and including patterns or shapes in addition to colors can enhance
            accessibility.
          </li>

          <li>
            <strong>Mobile Optimization:</strong> If the visualizations are not
            optimized for mobile devices, they may be difficult to view on
            smaller screens. Responsive design would ensure that the
            visualizations are effective across all devices.
          </li>

          <li>
            <strong>Contextual Information:</strong> The lack of contextual
            information may hinder deeper insights. Incorporating elements that
            provide context, like annotations, data source descriptions, or even
            a narrative storyline, could enrich the user&apos;s understanding.
          </li>
        </ol>

        <p>
          By addressing these aspects, the effectiveness of the visualizations
          could be greatly improved, making them not only more aesthetically
          pleasing but also more informative and easier to use for a wider
          audience.
        </p>
      </div>
    ),
  },
];

export function AntdTabs() {
  return (
    <div className="flex flex-col gap-y-5">
      <Tabs
        defaultActiveKey="1"
        type="card"
        size={"large"}
        items={descriptions}
        className="gap-x-3"
      />

      <h1 className="text-6xl text-center">Gallery</h1>
      <div>
        <Slide
          alt="selfie-exp"
          src="/selfie-exp.png"
          heading="The selfie exploratory visualization"
          description="Visualization is to analyze and present insights on the demographics, poses, features, and moods of people taking selfies in different urban environments."
        />
      </div>
      <div>
        <Slide
          alt="demographics"
          src="/demographics.png"
          heading="Demographics"
          description="The visualization likely includes data points like city, age, and gender. By mapping these variables, the project can demonstrate differences or similarities in selfie trends across locations and demographics. For example, it could reveal that selfies are more popular among younger populations or show varying trends between genders in different cities."
        />
      </div>
      <div>
        <Slide
          alt="features"
          src="/features.png"
          heading="Features"
          description="By examining facial features such as whether eyes are open or closed, mouth is open or closed, and presence of glasses, the project can deduce patterns in facial expressions and accessory use in selfies. This can lead to insights about emotional display norms and style preferences."
        />
      </div>
      <div>
        <Slide
          alt="pose"
          src="/pose.png"
          heading="Pose"
          description="The analysis of pose, including orientation (up, down, left, right) and head tilt, helps to understand common physical attitudes in selfies. This might uncover cultural preferences or individual behaviors associated with how people present themselves in self-portraits."
        />
      </div>
      <div>
        <Slide
          alt="mood"
          src="/mood.png"
          heading="Mood"
          description="The mood section with indicators such as calm, angry, and happy provides a quantifiable measure of the emotional tone conveyed in selfies. This could be correlated with cultural expressions of emotion or societal influences on behavior in different cities."
        />
      </div>
      <div>
        <Slide
          alt="selfies"
          src="/selfies.png"
          heading="Selfie Viz"
          description="The large dataset of selfies allows for comparative analysis and identification of prevalent trends. It serves as the empirical basis for the project’s findings."
        />
      </div>
    </div>
  );
}
