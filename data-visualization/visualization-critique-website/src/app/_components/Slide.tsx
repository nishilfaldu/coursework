import Image from "next/image";

export function Slide({
  heading,
  description,
  src,
  alt,
}: {
  heading: string;
  description: string;
  src: string;
  alt: string;
}) {
  return (
    <section className="text-gray-600 body-font flex justify-center flex-col items-center">
      <Image width={500} height={500} src={src} alt={alt} />
      <div className="text-center lg:w-2/3 w-full">
        <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
          {heading}
        </h1>
        <p className="mb-8 leading-relaxed">{description}</p>
      </div>
    </section>
  );
}
