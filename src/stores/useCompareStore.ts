import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Product } from '@/types';

interface CompareState {
  items: Product[];
  isOpen: boolean;
  addToCompare: (product: Product) => boolean;
  removeFromCompare: (productId: string) => void;
  clearCompare: () => void;
  toggleCompare: () => void;
  openCompare: () => void;
  closeCompare: () => void;
  isInCompare: (productId: string) => boolean;
}

export const useCompareStore = create<CompareState>()(
  persist(
    (set, get) => ({
      items: [],
      isOpen: false,

      addToCompare: (product) => {
        const { items } = get();
        if (items.some((p) => p.id === product.id)) {
          return false;
        }
        if (items.length >= 4) {
          alert('الحد الأقصى للمقارنة هو 4 أجهزة / Max 4 products for comparison');
          return false;
        }
        set({ items: [...items, product], isOpen: true });
        return true;
      },

      removeFromCompare: (productId) => {
        set((state) => ({
          items: state.items.filter((p) => p.id !== productId),
        }));
      },

      clearCompare: () => set({ items: [], isOpen: false }),
      toggleCompare: () => set((state) => ({ isOpen: !state.isOpen })),
      openCompare: () => set({ isOpen: true }),
      closeCompare: () => set({ isOpen: false }),

      isInCompare: (productId) => {
        return get().items.some((p) => p.id === productId);
      },
    }),
    {
      name: 'mess_tech_compare',
      partialize: (state) => ({ items: state.items }),
    }
  )
);
