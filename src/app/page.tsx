import HeroCarousel from '@/components/home/HeroCarousel';
import TrustBar from '@/components/home/TrustBar';
import CategoryBannerGrids from '@/components/home/CategoryBannerGrids';
import ProductGridSection from '@/components/home/ProductGridSection';
import FlashDeals from '@/components/home/FlashDeals';
import BrandsRibbon from '@/components/home/BrandsRibbon';

export default function HomePage() {
  return (
    <div className="w-full">
      {/* 1. Hero Panoramic Banner Slider */}
      <HeroCarousel />

      {/* 2. Trust Bar (COD, Fast Shipping, 100% Genuine, Warranty) */}
      <TrustBar />

      {/* 3. Category Banner Grids (Switches, WiFi, Storage / UPS, Attendance, Screens) */}
      <CategoryBannerGrids />

      {/* 4. Flash Deals with Live Countdown */}
      <FlashDeals />

      {/* 5. Featured Products Grid (Cisco, MikroTik, Ubiquiti, Synology, APC) */}
      <ProductGridSection />

      {/* 6. Partner Brands Ribbon */}
      <BrandsRibbon />
    </div>
  );
}
